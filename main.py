def write_xml_file(data, file_path):
    try:
        root = ET.Element("root")
        root.append(data)
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print("Dane zapisane do pliku XML.")
    except IOError as e:
        print(f"Błąd zapisu do pliku XML: {e}")

write_xml_file(xml_data, output_file)
