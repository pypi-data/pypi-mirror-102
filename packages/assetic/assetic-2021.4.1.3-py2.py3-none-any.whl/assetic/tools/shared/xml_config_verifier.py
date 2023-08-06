import datetime
import xml.dom.minidom

import assetic.assetic_sdk
from assetic.tools import APIHelper


class XMLConfigVerifier:
    def __init__(self, xml_fp, ini_fp, conf_output):

        # file path of the xml file
        self.fp = xml_fp

        # access to the sdk to call the API to check on things
        self.sdk = assetic.assetic_sdk.AsseticSDK(ini_fp)

        # api to call things
        self.api = APIHelper()

        # the file path of the final output
        self.conf_output = conf_output

        # error trackers
        self.errors = []
        self.warnings = []

        # a list to keep track of output lines
        self.output_values = [
            "###\tXML Configuration Report\t###\n",
            "Creation Date:\t{0}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        ]

        # attempt to read the xml file and return the dom
        self.dom = self.init_dom(xml_fp)

    def init_dom(self, fp):
        try:
            dom = xml.dom.minidom.parse(fp)
        except xml.parsers.expat.ExpatError:
            self.errors.append("FATAL: File [{0}] is inappropriately formed. Ensure that all tags "
                               "(elements contained within brackets, e.g. <tag>tag-contents</tag>)"
                               " have starting and ending brackets.".format(fp))
            return None

        return dom

    @staticmethod
    def get_element(element, tag):
        els = element.getElementsByTagName(tag)
        if len(els) == 0:
            raise TypeError
        elif len(els) > 1:
            raise TypeError

        return els[0]

    def get_attributes(self, lyr, tagname):
        try:
            fields = self.get_element(lyr, tagname)
        except TypeError:
            # e.g. the node is not defined
            return {}

        mps = {}
        for attr in fields.childNodes:
            if type(attr) == xml.dom.minidom.Text:
                continue

            try:
                mps[attr.tagName] = attr.childNodes[0].nodeValue
            except IndexError:
                pass

        return mps

    def output(self, mode="w"):
        with open(self.conf_output, mode) as f:
            f.write("\n".join(self.output_values))

    def parse_fls(self, fl_mappings):
        """
        Functional locations require EITHER:
            -   Functional Location Friendly ID
                    OR
            -   Functional Location Name, and
            -   Functional Location Type
        """

        if len(fl_mappings) == 0:
            return

        if "functional_location_id" in fl_mappings.keys():
            return

        if "functional_location_name" not in fl_mappings.keys():
            self.errors.append("FUNCTIONAL LOCATION: Functional location name (in addition "
                               "to functional location type) must be defined in configuration"
                               " file if `functional_location_id` not defined.")

        if "functional_location_type" not in fl_mappings.keys():
            self.errors.append("FUNCTIONAL LOCATION: Functional location type (in addition "
                               "to functional location name) must be defined in configuration"
                               " file if `functional_location_id` not defined.")

    def get_creation_status(self, layer):
        valid = ["Active", "Disposed", "Decommissioned", "Out of Sysem"]

        try:
            val = self.get_element(layer, "creation_status")
            cs = val.childNodes[0].nodeValue
        except TypeError:
            self.warnings.append("CREATION STATUS: No creation status for layer {0} defined. "
                                 "Will default to 'Active'.")
            cs = "Active"

        if cs not in valid:
            self.errors.append("CREATION STATUS: Creation status [{0}] is not a valid status. "
                               "Valid statuses: {1}".format(cs, valid))
        return cs

    def get_upload_feature(self, layer):
        try:
            val = self.get_element(layer, "upload_feature")
        except TypeError:
            return False

        self.warnings.append("SPATIAL: Upload Feature tag (<upload_feature>True/False"
                             "</upload_feature> set to False. No spatial information will "
                             "be uploaded against features for this layer.")
        return str(val.childNodes[0].nodeValue).upper() == "TRUE"

    def get(self, element, attr):
        el = self.get_element(element, attr)
        return el.childNodes[0].nodeValue

    def get_logfile_loc(self, dom):
        el = self.get_element(dom, "logfile")
        return el.childNodes[0].nodeValue

    def display_layer_attr_info(self, i, lyr, mappings):
        self.add_to_output("Layer {0}: {1}".format(i, lyr.getAttribute("name")))

        upload = self.get_upload_feature(lyr)
        self.add_to_output("Upload spatial information for asset: {0}".format(upload), num_tabs=1)
        creation_status = self.get_creation_status(lyr)
        self.add_to_output("Asset status on creation: {0}".format(creation_status), num_tabs=1)

        for val, m in mappings.items():
            self.display_attrs(val, m)

    def display_attrs(self, title, mappings, num_tabs=1):
        self.add_to_output(title, num_tabs=num_tabs)
        if len(mappings) == 0:
            self.add_to_output("\t*\tno values defined\t*", num_tabs=num_tabs)
            return
        for k, v in mappings.items():
            self.add_to_output("\t-\t{0}: {1}".format(k, v), num_tabs=num_tabs)

    def add_to_output(self, msg, num_tabs=0):
        tabs = "".join(["\t" for _ in range(num_tabs)])
        self.output_values.append("{0}{1}".format(tabs, msg))

    def parse_address_fields(self, fields, defs):
        keys = list(fields.keys()) + list(defs.keys())

        if len(keys) == 0:
            return

        if "country" not in keys:
            self.errors.append("ADDRESS: The minimum information required for "
                               "address definitions is the value 'Country'. "
                               "Values currently defined: {0}".format(keys))

    def display_cp_info(self, cp_mappings):
        self.add_to_output("Component", num_tabs=1)
        for val, m in cp_mappings.items():
            self.display_attrs(val, m, num_tabs=2)

    def display_dimension_info(self, d_mappings, j):
        self.add_to_output("Dimension {0}".format(j), num_tabs=3)
        for val, m in d_mappings.items():
            self.display_attrs(val, m, num_tabs=4)

    def flush_errors(self):
        msg = ("There were errors while parsing the XML configuration file.\n\n"
               "Creation date: {0}\n\n"
               "###\tERRORS\t###\n\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        for e in self.errors:
            msg += "{0}".format(e)

        msg += "These need to be fixed before the integration will work properly."

        with open(self.conf_output, "w") as f:
            f.write(msg)

    def run(self):

        if self.dom is None:
            # there was an initilisation error
            self.flush_errors()
            return

        lf_loc = self.get(self.dom, "logfile")
        lf_level = self.get(self.dom, "loglevel")

        intro = ("### Assetic GIS Integration XML Configuration Parser ###\n\n"
                 "Logfile location:     {0}\n"
                 "Loglevel:             {1}\n"
                 "XML location:         {2}\n"
                 .format(lf_loc, lf_level, self.fp)
                 )
        self.add_to_output(intro)

        r = self.api.generic_get("/api/v2/assetcategory/")
        valid_cat_labels = [l["Label"] for l in r["ResourceList"]]

        asset = None

        ops = self.dom.getElementsByTagName("operation")
        for o in ops:
            if o.getAttribute("action") == "Asset":
                asset = o
                break
        if asset is None:
            self.errors.append("FATAL: No asset layers defined.")

        layers = asset.getElementsByTagName("layer")

        self.add_to_output("Present Asset Layers:")
        for i, l in enumerate(layers, start=1):
            self.add_to_output("\t{0}.\t{1}".format(i, l.getAttribute("name")))
        self.add_to_output("")

        for i, layer in enumerate(layers, start=1):
            cat_node = self.get_element(layer, "category")
            cat = cat_node.firstChild.nodeValue
            if cat not in valid_cat_labels:
                self.errors.append("CATEGORY: [{0}] is not present in Assetic environment. "
                                   "Check Asset Register ({1}/Admin/AssetRegister/) "
                                   "to ensure the category has been enabled or is "
                                   "spelled/formatted correctly".format(cat, self.api.host))

            asset_mappings = {
                "Asset Core Fields": self.get_attributes(layer, "corefields"),
                "Asset Core Defaults": self.get_attributes(layer, "coredefaults"),
                "Asset Attributes": self.get_attributes(layer, "attributefields"),
                "Asset Attribute Defaults": self.get_attributes(layer, "attributedefaults"),
            }

            addr_fields = self.get_attributes(layer, "addressfields")
            addr_defs = self.get_attributes(layer, "addressdefaults")

            self.parse_address_fields(addr_fields, addr_defs)

            asset_mappings.update({"Address Fields": addr_fields, "Address Defaults": addr_defs})
            fls = self.get_attributes(layer, "functional_location")
            self.parse_fls(fls)
            asset_mappings["Functional Location Definition"] = fls

            self.display_layer_attr_info(i, layer, asset_mappings)

            self.add_to_output("")

            cps = layer.getElementsByTagName("component")
            for cp in cps:
                cp_mappings = {
                    "Component Fields": self.get_attributes(cp, "componentfields"),
                    "Component Defaults": self.get_attributes(cp, "componentdefaults")
                }
                self.display_cp_info(cp_mappings)
                dims = cp.getElementsByTagName("dimension")
                self.add_to_output("Dimensions ({0})".format(len(dims)), num_tabs=2)
                if len(dims) == 0:
                    self.add_to_output("*\tno values defined\t*", num_tabs=3)
                for j, d in enumerate(dims, start=1):
                    d_mappings = {
                        "Dimension Fields": self.get_attributes(d, "dimensionfields"),
                        "Dimension Defaults": self.get_attributes(d, "dimensiondefaults")
                    }
                    self.display_dimension_info(d_mappings, j)

        if len(self.errors) > 0:
            self.flush_errors()
            self.output(mode="a")
        else:
            self.output(mode="w")


if __name__ == '__main__':
    xmlfile = r"C:\repos\gis\assetic_qgis_sdk\user_config_files\gis_jan.xml"
    inifile = r"C:\repos\test.ini"
    logfile = r"C:\repos\assetic_qgis_sdk\log.txt"

    _conf_output = r"C:\repos\conf_output.txt"
    x = XMLConfigVerifier(xmlfile, inifile, _conf_output)
    x.run()
