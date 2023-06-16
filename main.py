import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import py_compile

def check_syntax(file_path):
    try:
        compile(open(file_path, "rb").read(), file_path, 'exec')
        return True
    except SyntaxError:
        return False

class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Data Converter')
        self.setGeometry(100, 100, 400, 150)

        main_widget = QWidget()
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.input_label = QLabel('Input File:')
        self.input_line_edit = QLineEdit()
        self.input_button = QPushButton('Browse...')
        self.input_button.clicked.connect(self.browse_input_file)

        self.output_label = QLabel('Output File:')
        self.output_line_edit = QLineEdit()
        self.output_button = QPushButton('Browse...')
        self.output_button.clicked.connect(self.browse_output_file)

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_files)

        layout.addWidget(self.input_label)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.input_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_line_edit)
        layout.addWidget(self.output_button)
        layout.addWidget(self.convert_button)

        self.setCentralWidget(main_widget)

    def browse_input_file(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        input_file = file_dialog.getOpenFileName()[0]
        self.input_line_edit.setText(input_file)

    def browse_output_file(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        output_file = file_dialog.getSaveFileName()[0]
        self.output_line_edit.setText(output_file)

    def convert_files(self):
        input_file = self.input_line_edit.text()
        output_file = self.output_line_edit.text()
        try:
            convert_file(input_file, output_file)
            QMessageBox.information(self, 'Success', 'Conversion completed successfully.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))



def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path)

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

    main_file = __file__
    if not check_syntax(main_file):
        print(f"Błąd składni w pliku: {main_file}")
        sys.exit(1)


    imported_modules = [argparse, json, yaml, ET]
    for module in imported_modules:
        module_file = module.__file__ if hasattr(module, '__file__') else None
        if module_file and not check_syntax(module_file):
            print(f"Błąd składni w pliku: {module_file}")
            sys.exit(1)


    if len(sys.argv) > 1:
        run_from_command_line()
    else:
        run_with_ui()
