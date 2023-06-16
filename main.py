def convert_file(input_file, output_file):
    if input_file.endswith('.json'):
        data = load_json(input_file)
        if output_file.endswith('.yml') or output_file.endswith('.yaml'):
            save_yaml(data, output_file)
        elif output_file.endswith('.xml'):
            save_xml(data, output_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
        if output_file.endswith('.json'):
            save_json(data, output_file)
        elif output_file.endswith('.xml'):
            save_xml(data, output_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
        if output_file.endswith('.json'):
            save_json(data, output_file)
        elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
            save_yaml(data, output_file)
    else:
        raise ValueError('Invalid input file format.')

def run_with_ui():
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())

def run_from_command_line():
    args = parse_arguments()
    convert_file(args.input_file, args.output_file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_from_command_line()
    else:
        run_with_ui()
