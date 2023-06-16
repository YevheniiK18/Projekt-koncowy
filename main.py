def write_xml_file(data, file_path):
    root = ET.Element("root")
    root.append(data)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Data saved to XML file.")

write_xml_file(xml_data, output_file)
