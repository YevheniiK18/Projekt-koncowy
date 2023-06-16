import sys
import json
import yaml
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QFileDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        self.layout = QVBoxLayout()
        self.label = QLabel("Wprowadź ścieżki do plików lub użyj przycisków, aby wczytać lub zapisać dane.")
        self.load_button = QPushButton("Wczytaj")
        self.save_button = QPushButton("Zapisz")
        self.load_button.clicked.connect(self.load_data)
        self.save_button.clicked.connect(self.save_data)
        self.file_path_input = QLineEdit()
        self.save_file_path_input = QLineEdit()
        self.layout.addWidget(self.label)
        self.layout.addWidget(QLabel("Ścieżka pliku do wczytania:"))
        self.layout.addWidget(self.file_path_input)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(QLabel("Ścieżka pliku do zapisu:"))
        self.layout.addWidget(self.save_file_path_input)
        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def load_data(self):
        file_path = self.file_path_input.text()
        if not file_path:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "Wczytaj plik", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yml);;XML Files (*.xml)", options=options)
            if not file_path:
                return

        self.file_path_input.setText(file_path)

        try:
            if file_path.endswith('.json'):
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    self.label.setText(f'Wczytano dane z pliku JSON: {data}')
            elif file_path.endswith('.yml'):
                with open(file_path, 'r') as yaml_file:
                    data = yaml.safe_load(yaml_file)
                    self.label.setText(f'Wczytano dane z pliku YAML: {data}')
            elif file_path.endswith('.xml'):
                tree = ET.parse(file_path)
                root = tree.getroot()
                self.label.setText(f'Wczytano dane z pliku XML: {root.tag}')
            else:
                self.label.setText('Nieobsługiwany format pliku')
        except Exception as e:
            self.label.setText(f'Błąd wczytywania pliku: {str(e)}')

        self.label.setText('Operacja zrobiona')

    def save_data(self):
        save_file_path = self.save_file_path_input.text()
        if not save_file_path:
            options = QFileDialog.Options()
            save_file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yml);;XML Files (*.xml)", options=options)
            if not save_file_path:
                return

        self.save_file_path_input.setText(save_file_path)

        try:
            if save_file_path.endswith('.json'):
                data = {'example': 'data'}
                with open(save_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                self.label.setText('Dane zapisano do pliku JSON')
            elif save_file_path.endswith('.yml'):
                data = {'example': 'data'}
                with open(save_file_path, 'w') as yaml_file:
                    yaml.dump(data, yaml_file)
                self.label.setText('Dane zapisano do pliku YAML')
            elif save_file_path.endswith('.xml'):
                root = ET.Element('root')
                ET.SubElement(root, 'example').text = 'data'
                tree = ET.ElementTree(root)
                tree.write(save_file_path)
                self.label.setText('Dane zapisano do pliku XML')
            else:
                self.label.setText('Nieobsługiwany format pliku')
        except Exception as e:
            self.label.setText(f'Błąd zapisu do pliku: {str(e)}')

        self.label.setText('Operacja zrobiona')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
