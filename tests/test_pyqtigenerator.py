# test_pyqtigenerator.py

from PyQTIGenerator import PyQTIGenerator

# Create an instance of the class
generator = PyQTIGenerator('../PyQTIGenerator/data/imsmanifest.xml')

# Test the functionality
xml_output = generator.get_xml()

# Print the output
print(xml_output)

