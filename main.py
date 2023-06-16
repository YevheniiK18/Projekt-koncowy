import json
import yaml
import xml.etree.ElementTree as ET
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog

class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.setGeometry(100, 100, 300, 150)

        self.input_label = QLabel("Input File:", self)
        self.input_field = QLineEdit(self)
        self.input_button = QPushButton("Browse", self)
        self.input_button.clicked.connect(self.browse_input)

        self.output_label = QLabel("Output File:", self)
        self.output_field = QLineEdit(self)
        self.output_button = QPushButton("Browse", self)
        self.output_button.clicked.connect(self.browse_output)

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_data)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.input_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)
        layout.addWidget(self.output_button)
        layout.addWidget(self.convert_button)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def browse_input(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Input File")
        if file_path:
            self.input_field.setText(file_path)

    def browse_output(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Select Output File")
        if file_path:
            self.output_field.setText(file_path)

    def convert_data(self):
        input_file = self.input_field.text()
        output_file = self.output_field.text()

        if input_file.endswith('.json'):
            json_data = self.read_json_file(input_file)
            if json_data:
                self.write_json_file(json_data, output_file)

        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            yaml_data = self.read_yaml_file(input_file)
            if yaml_data:
                self.write_yaml_file(yaml_data, output_file)

        elif input_file.endswith('.xml'):
            xml_data = self.read_xml_file(input_file)
            if xml_data:
                self.write_xml_file(xml_data, output_file)

        else:
            self.show_message_box("Unsupported File Format")

    def read_json_file(self, file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError as e:
                self.show_message_box(f"Error decoding JSON file: {e}")
                return None

    def write_json_file(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        self.show_message_box("Data saved to JSON file.")

    def read_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            try:
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as e:
                self.show_message_box(f"Error parsing YAML file: {e}")
                return None

    def write_yaml_file(self, data, file_path):
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
        self.show_message_box("Data saved to YAML file.")

    def read_xml_file(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            return root
        except ET.ParseError as e:
            self.show_message_box(f"Error parsing XML file: {e}")
            return None

    def write_xml_file(self, data, file_path):
        root = ET.Element("root")
        root.append(data)
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        self.show_message_box("Data saved to XML file.")

    def show_message_box(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Message")
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())
