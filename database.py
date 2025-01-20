import sqlite3

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect("skincare.db")  # Creates a database file named skincare.db
    return conn

# Function to initialize the database
def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Create a table for skincare products
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            skin_type TEXT NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to add a product
def add_product(name, type, skin_type, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (name, type, skin_type, description)
        VALUES (?, ?, ?, ?)
    """, (name, type, skin_type, description))

    conn.commit()
    conn.close()

# Function to retrieve products for a specific skin type
def get_products_by_skin_type(skin_type):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, type, description FROM products WHERE skin_type = ?
    """, (skin_type,))

    results = cursor.fetchall()
    conn.close()

    return results
