import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)


class CrudApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Update")
        self.setFixedSize(300, 360)

        self.db = sqlite3.connect("users.db")
        self.cursor = self.db.cursor()
        self.create_table()

        self.init_ui()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        """)
        self.db.commit()

    def init_ui(self):
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID пользователя")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Возраст")

        self.status = QLabel("")

        btn_add = QPushButton("Добавить")
        btn_add.clicked.connect(self.add_user)

        btn_update = QPushButton("Обновить")
        btn_update.clicked.connect(self.update_user)

        btn_delete = QPushButton("Удалить")
        btn_delete.clicked.connect(self.delete_user)

        btn_read = QPushButton("Read Users")
        btn_read.clicked.connect(self.read_users)

        layout = QVBoxLayout()
        layout.addWidget(self.id_input)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(btn_add)
        layout.addWidget(btn_update)
        layout.addWidget(btn_delete)
        layout.addWidget(btn_read)
        layout.addWidget(self.status)

        self.setLayout(layout)

    def add_user(self):
        name = self.name_input.text()
        age = self.age_input.text()

        if not name or not age:
            self.status.setText("Заполните имя и возраст")
            return

        self.cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, age)
        )
        self.db.commit()

        self.status.setText("Пользователь добавлен")
        self.clear_inputs()

    def read_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()

        if not users:
            self.status.setText("Таблица пустая")
            return

        text = ""
        for user in users:
            text += f"{user[0]} | {user[1]} | {user[2]}\n"

        self.status.setText(text)

    def update_user(self):
        user_id = self.id_input.text()
        name = self.name_input.text()
        age = self.age_input.text()

        if not user_id or not name or not age:
            self.status.setText("Нужны ID, имя и возраст")
            return

        self.cursor.execute(
            "UPDATE users SET name=?, age=? WHERE id=?",
            (name, age, user_id)
        )
        self.db.commit()

        if self.cursor.rowcount == 0:
            self.status.setText("Пользователь не найден")
        else:
            self.status.setText("Пользователь обновлён")
            self.clear_inputs()

    def delete_user(self):
        user_id = self.id_input.text()

        if not user_id:
            self.status.setText("Введите ID")
            return

        self.cursor.execute(
            "DELETE FROM users WHERE id=?",
            (user_id,)
        )
        self.db.commit()

        if self.cursor.rowcount == 0:
            self.status.setText("Пользователь не найден")
        else:
            self.status.setText("Пользователь удалён")
            self.clear_inputs()

    def clear_inputs(self):
        self.id_input.clear()
        self.name_input.clear()
        self.age_input.clear()

    def closeEvent(self, event):
        self.db.close()
        event.accept()


app = QApplication(sys.argv)
window = CrudApp()
window.show()
sys.exit(app.exec())
