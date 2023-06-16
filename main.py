import xml.etree.ElementTree as ET

data = ET.Element('root')
child = ET.SubElement(data, 'child')
child.text = 'Tekst'

def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    with open(file_path, 'wb') as file:
        tree.write(file)

file_path = 'plik.xml'
save_xml(data, file_path)
