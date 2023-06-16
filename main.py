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

        thread = ConvertThread(input_file, output_file)
        thread.conversion_finished.connect(self.on_conversion_finished)
        thread.start()
