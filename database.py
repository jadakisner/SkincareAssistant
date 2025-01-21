import sqlite3

def initialize_db():
    conn = sqlite3.connect("skincare.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL,
            skin_type TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, type, skin_type, description):
    conn = sqlite3.connect("skincare.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO products (name, type, skin_type, description)
            VALUES (?, ?, ?, ?)
        ''', (name, type, skin_type, description))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Avoid duplicate entries
    conn.close()

def get_products_by_skin_type(skin_type):
    conn = sqlite3.connect("skincare.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT DISTINCT name, type, description FROM products WHERE skin_type = ?
    ''', (skin_type,))
    products = list(set(cursor.fetchall()))  # Ensure unique results
    conn.close()
    return products