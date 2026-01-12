from database import get_connection
import sqlite3

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE,
        )
    """)
    conn.commit()
    conn.close()

def add_category(name):
    try:
        conn = get_connection()
        conn.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Такая категория уже существует")
    finally:
        conn.close()

def get_categories():
    conn = get_connection()
    data = conn.execute("SELECT id, name FROM categories").fetchall()
    conn.close()
    return data

def add_product(name, category_id):
    conn = get_connection()
    conn.execute(
        "INSERT INTO products (name, category_id) VALUES (?, ?)",
        (name, category_id)
    )
    conn.commit()
    conn.close()

def get_products(category_id):
    conn = get_connection()
    data = conn.execute("""
        SELECT products.id, products.name, products.category_id = categories.id
        FROM products
        JOIN categories ON products.category_id = categories.id
        ORDER BY products.id DESC
    """).fetchall()
    conn.close()
    return data

def delete_product(product_id):
    conn = get_connection()
    conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def update_product(product_id, new_name, new_category_id):
    conn = get_connection()
    conn.execute(
        "UPDATE products SET name = ?, category_id = ? WHERE id = ?",
        (new_name, new_category_id, product_id)
    )
    conn.commit()
    conn.close()

def search_product(text):
    conn = get_connection()
    data = conn.execute("""
        SELECT products.id, products.name, categories.name
        FROM products
        JOIN categories ON products.category_id = categories.id
        WHERE products.name LIKE ?
    """, (f"%{text}%",)).fetchall()
    conn.close()
    return data








