from PyQt5.QtCore import Qt, QThread, pyqtSignal

class ConvertThread(QThread):
    conversion_finished = pyqtSignal()

    def __init__(self, input_file, output_file):
        super().__init__()
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        # Wykonaj odpowiednie zadanie konwersji (Task2-Task7) z kodu powyżej
        # Na końcu, emituj sygnał conversion_finished
        self.conversion_finished.emit()

    def convert_data(self):
        thread = ConvertThread(input_file, output_file)
        thread.conversion_finished.connect(self.on_conversion_finished)
        thread.start()

    def on_conversion_finished(self):
        self.show_message_box("Conversion finished.")
