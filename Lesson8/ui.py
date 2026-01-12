from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QComboBox, QListWidget,
    QMessageBox, QMainWindow
)

from models import (
    add_category, get_categories,
    add_product, get_products,
    delete_product, update_product,
    search_product
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Lesson 8")
        self.setMinimumSize(500, 450)

        self.editing_product_id = None

        self.layout = QVBoxLayout()

        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Название категории")

        self.add_category_btn = QPushButton("Добавить категорию")
        self.add_category_btn.clicked.connect(self.create_category)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск товара")
        self.search_input.textChanged.connect(self.search)

        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Название товара")

        self.category_box = QComboBox()
        self.load_categories()

        self.add_product_btn = QPushButton("Добавить товар")
        self.add_product_btn.clicked.connet(self.create_product)

        self.list_widget = QListWidget()
        self.load_products()

        self.edit_btn = QPushButton("Редактировать")
        self.edit_btn.clicked.connect(self.load_to_edit)

        self.save_btn = QPushButton("Сохранить изменения")
        self.save_btn.clicked.connect(self.save_edit)

        self.delete_btn = QPushButton("Удалить")
        self.delete_btn.clicked.connect(self.remove_product)