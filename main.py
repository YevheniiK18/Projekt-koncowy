
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
    def convert_data_async(input_file, output_file):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            if input_file.endswith('.json'):
                read_future = executor.submit(read_json_file, input_file)
                json_data = read_future.result()
                write_future = executor.submit(write_json_file, json_data, output_file)
                write_future.result()

            elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
                read_future = executor.submit(read_yaml_file, input_file)
                yaml_data = read_future.result()
                write_future = executor.submit(write_yaml_file, yaml_data, output_file)
                write_future.result()

            elif input_file.endswith('.xml'):
                read_future = executor.submit(read_xml_file, input_file)
                xml_data = read_future.result()
                write_future = executor.submit(write_xml_file, xml_data, output_file)
                write_future.result()

            else:
                print("Nieobsługiwany format pliku.")

            print("Konwersja zakończona.")

    app = QApplication(sys.argv)
    window = ConverterApp()
    window.convert_button.clicked.connect(lambda: convert_data_async(window.input_field.text(), window.output_field.text()))
    window.show()
    sys.exit(app.exec())
