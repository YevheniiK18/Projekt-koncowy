def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path)
