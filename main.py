 def convert_data(self):
        input_file = self.input_field.text()
        output_file = self.output_field.text()

        if input_file.endswith('.json'):
            json_data = read_json_file(input_file)
            if json_data:
                write_json_file(json_data, output_file)

        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            yaml_data = read_yaml_file(input_file)
            if yaml_data:
                write_yaml_file(yaml_data, output_file)

        elif input_file.endswith('.xml'):
            xml_data = read_xml_file(input_file)
            if xml_data:
                write_xml_file(xml_data, output_file)

        else:
            print("Nieobsługiwany format pliku.")

        print("Konwersja zakończona.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())

