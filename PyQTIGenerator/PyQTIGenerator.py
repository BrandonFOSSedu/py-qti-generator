from lxml import objectify, etree
from copy import deepcopy

class PyQTIGenerator:
    def __init__(self, xmlfile):
        self.tree = objectify.parse(xmlfile)
        self.root = self.tree.getroot()

    def get_xml(self):
        # Remove objectify annotations
        xml_tree = deepcopy(self.root)
        objectify.deannotate(xml_tree, xsi_nil=True)
        etree.cleanup_namespaces(xml_tree)

        # Convert the objectify tree back into XML string
        xml_string = etree.tostring(xml_tree, pretty_print=True).decode('utf-8')

        print(xml_string)

