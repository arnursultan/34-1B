import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox,
    QLabel
)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")
conn.commit()

class CrudApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD App Lesson 5-6")
        self.setGeometry(300, 200, 400, 500)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("CRUD приложение PyQt6 + SQLite")
        self.setStyleSheet("""
            QPushButton {
                background-color: #ff69b4;
                color: white;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #ff1493;
            }

            QPushButton:pressed {
                background-color: #e60073;
            }
        """)

        self.search_label = QLabel("Поиск по имени")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите имя")
        self.search_input.textChanged.connect(self.search_user)

        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя пользователя")

        self.age_label = QLabel("Возраст:")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Возраст пользователя")

        self.add_btn = QPushButton("Добавить")
        self.delete_btn = QPushButton("Удалить выбранное")

        self.list_label = QLabel("Список пользователей:")
        self.list_widget = QListWidget()

        self.status_label = QLabel("Записей в базе: 0")

        self.layout.addWidget(self.title_label)

        self.layout.addWidget(self.search_label)
        self.layout.addWidget(self.search_input)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)

        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.delete_btn)

        self.layout.addWidget(self.list_label)
        self.layout.addWidget(self.list_widget)

        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

        self.add_btn.clicked.connect(self.add_user)
        self.delete_btn.clicked.connect(self.delete_user)

        self.load_users()

    def add_user(self):
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()

        if not name or not age:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        if not age.isdigit():
            QMessageBox.warning(self, "Ошибка", "Возраст должен быть числом")
            return

        cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, int(age))
        )
        conn.commit()

        self.name_input.clear()
        self.age_input.clear()
        self.load_users()

    def load_users(self):
        self.list_widget.clear()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        for user in users:
            self.list_widget.addItem(
                f"{user[0]} | {user[1]} | {user[2]}",
            )

            self.status_label.setText(f"Записей в базе: {len(users)}")

    def search_user(self):
        text = self.search_input.text()
        self.list_widget.clear()

        cursor.execute("SELECT * FROM users WHERE name LIKE ?",
                       (f"%{text}%",)
        )

        users = cursor.fetchall()
        for user in users:
            self.list_widget.addItem(
                f"{user[0]} | {user[1]} | {user[2]}",
            )

        self.status_label.setText(f"Найдено записей: {len(users)}")

    def delete_user(self):
        selected_item = self.list_widget.currentItem()

        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите запись")
            return

        user_id = selected_item.text().split("|")[0]

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        conn.commit()
        self.load_users()

app = QApplication(sys.argv)
window = CrudApp()
window.show()
sys.exit(app.exec())