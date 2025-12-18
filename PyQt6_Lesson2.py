# Code №1
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle("Первое окно!")
# # window.resize(400, 300)
# window.setFixedSize(400, 300)
# window.show()
#
# sys.exit(app.exec())

# Code №2
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyQt6 - Урок 2")
        self.resize(400, 250)

        self.label = QLabel("Введите текст:")
        self.input = QLineEdit()
        self.button = QPushButton("Показать")
        self.result = QLabel("")

        self.button.clicked.connect(self.show_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def show_text(self):
        text = self.input.text()
        self.result.setText(f"Вы ввели: {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()