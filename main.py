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
