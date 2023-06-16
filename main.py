from PyQt5.QtWidgets import QFileDialog

class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter danych")
        self.setGeometry(100, 100, 300, 150)

        self.input_label = QLabel("Plik wejściowy:", self)
        self.input_field = QLineEdit(self)

        self.output_label = QLabel("Plik wyjściowy:", self)
        self.output_field = QLineEdit(self)

        self.select_input_button = QPushButton("Wybierz plik wejściowy", self)
        self.select_input_button.clicked.connect(self.select_input_file)

        self.select_output_button = QPushButton("Wybierz plik wyjściowy", self)
        self.select_output_button.clicked.connect(self.select_output_file)

        self.convert_button = QPushButton("Konwertuj", self)
        self.convert_button.clicked.connect(self.convert_data)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.select_input_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)
        layout.addWidget(self.select_output_button)
        layout.addWidget(self.convert_button)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy")
        if file_path:
            self.input_field.setText(file_path)

    def select_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Wybierz plik wyjściowy")
        if file_path:
            self.output_field.setText(file_path)
