import xml.etree.ElementTree as ET

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f'Błąd parsowania pliku XML: {e}')
        return None

file_path = 'plik.xml'
root = load_xml(file_path)
if root:

    print(root)
