# Основные виджеты PyQt6
# QWidget - Базовый Контейнер
# QLabel - Текст
# QPushButton - Кнопка
# QLineEdit - Поле ввода
# QTextEdit - Многострочный текст
# QVBoxLayout - Вертикальное расположение
# QHBoxLayout - Горизонтальное расположение
# QApplication - программа, которая управляет всеми окнами
from PyQt6_Lesson2 import main

# Code №1
# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QPushButton,
#     QLineEdit,
#     QVBoxLayout,
# )
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("PyQt6 Lesson 3")
#         self.setGeometry(800, 400, 400, 250)
#
#         self.label = QLabel("Введите имя:")
#         self.input_name = QLineEdit()
#         self.input_name.setPlaceholderText("Имя")
#
#         self.button = QPushButton("Поздороваться")
#         self.button.clicked.connect(self.say_hello)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.input_name)
#         layout.addWidget(self.button)
#
#         self.setLayout(layout)
#
#     def say_hello(self):
#         name = self.input_name.text()
#         if name:
#             self.label.setText(f"Привет, {name}!")
#         else:
#             self.label.setText("Введите имя!")
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())

# Code №2
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout
)
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🧮 Калькулятор")
        self.setFixedSize(300, 400)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("""
            font-size: 26px;
            padding: 10px;
            background-color: #1e1e1e;
            color: white;
            border-radius: 10px;
        """)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 50)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    background-color: #2d2d2d;
                    color: white;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #444;
                }
            """)
            button.clicked.connect(self.on_button_click)

            if text == "C":
                grid.addWidget(button, row, col, 1, 4)
            else:
                grid.addWidget(button, row, col)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Ошибка")
        else:
            self.display.setText(self.display.text() + text)


app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
