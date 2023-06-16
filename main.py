import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
import concurrent.futures

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Błąd dekodowania pliku JSON: {e}")
            return None

def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Dane zapisane do pliku JSON.")

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Błąd parsowania pliku YAML: {e}")
            return None

def write_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
    print("Dane zapisane do pliku YAML.")

def read_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd parsowania pliku XML: {e}")
        return None

def write_xml_file(data, file_path):
    root = ET.Element("root")
    root.append(data)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Dane zapisane do pliku XML.")


class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter danych")
        self.setGeometry(100, 100, 300, 150)

        self.input_label = QLabel("Plik wejściowy:", self)
        self.input_field = QLineEdit(self)
        self.input_button = QPushButton("Wybierz plik", self)
        self.input_button.clicked.connect(self.select_input_file)

        self.output_label = QLabel("Plik wyjściowy:", self)
        self.output_field = QLineEdit(self)
        self.output_button = QPushButton("Wybierz plik", self)
        self.output_button.clicked.connect(self.select_output_file)

        self.convert_button = QPushButton("Konwertuj", self)
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

    def select_input_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Wybierz plik wejściowy")
        self.input_field.setText(file_path)

    def select_output_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Wybierz plik wyjściowy")
        self.output_field.setText(file_path)

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
