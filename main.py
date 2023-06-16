def read_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None

xml_data = read_xml_file(input_file)
if xml_data is None:
    sys.exit(1)
