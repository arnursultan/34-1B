# import sqlite3
#
# conn = sqlite3.connect("database.sqlite3")
# cursor = conn.cursor()
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS zebra (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
# )
# """)
#
# cursor.execute("INSERT into zebra (name, age) VALUES (?,?) ", ("Marty", 10))
# conn.commit()
#
# cursor.execute("SELECT * FROM zebra")
# for row in cursor.fetchall():
#     print(row)
#
# conn.close()

import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)

class UserApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Урок 4 — PyQt6 + SQLite")
        self.setGeometry(300, 200, 400, 250)

        self.label = QLabel("Введите имя:")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Имя")

        self.button = QPushButton("Сохранить в БД")
        self.button.clicked.connect(self.save_to_db)

        self.result = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        self.setLayout(layout)

        self.init_db()

    def init_db(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def save_to_db(self):
        name = self.input_name.text()

        if not name:
            self.result.setText("Введите имя!")
            return

        self.cursor.execute(
            "INSERT INTO users (name) VALUES (?)",
            (name,)
        )
        self.conn.commit()

        self.result.setText(f"Имя '{name}' сохранено!")
        self.input_name.clear()

app = QApplication(sys.argv)
window = UserApp()
window.show()
sys.exit(app.exec())
