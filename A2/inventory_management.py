"""
Inventory Management System
-------------------------------
Name: Akshat verma
Roll No: 002311001001

Team Members:
- Daniyal Anis, Roll No: 002311001022
- Atin Roy, Roll No: 002311001023

This is a simple Inventory Management System that allows store owners to manage products and track purchase history. Customers can make purchases, while sellers can update product information. The system uses SQLite as a database and is tracked using Git for version control.
"""

import sqlite3

# Connect to sqlite database. It will create a new one if it does not exist
conn = sqlite3.connect("inventory_management.db")
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchase_history (
            transaction_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            FOREIGN KEY(product_id) REFERENCES products(product_id) ON DELETE CASCADE
        )
    ''')
    conn.commit()

# Function to add a product
def add_product(name, quantity, price):
    cursor.execute('''
        INSERT INTO products (name, quantity, price)
        VALUES (?, ?, ?)
    ''', (name, quantity, price))
    conn.commit()

# Function to update products' quantity
def update_quantity(product_id, quantity):
    cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE product_id = ?
    ''', (quantity, product_id))
    conn.commit()

# Function to make a purchase
def make_purchase(product_id, quantity):
    cursor.execute('SELECT quantity, price FROM products WHERE product_id = ?', (product_id,))
    product = cursor.fetchone()

    # Check if product is available
    if product:
        stock_quantity, price = product
        # Check if quantity is enough
        if stock_quantity >= quantity:
            total_price = quantity * price
            # After purchase, insert into purchase history table
            cursor.execute('''
                INSERT INTO purchase_history (product_id, quantity, total_price)
                VALUES (?, ?, ?)
            ''', (product_id, quantity, total_price))

            # Update the product quantity
            new_quantity = stock_quantity - quantity
            update_quantity(product_id, new_quantity)
            conn.commit()

            print(f"Purchase successful! Total price: ${total_price:.2f}")
        else:
            print("Not enough stock available.")
    else:
        print("Product not available.")

# Function to display all products
def display_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    print("Product ID | Name | Quantity | Price")
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | ${product[3]:.2f}")

# Function to display purchase history
def show_purchase_history():
    cursor.execute('SELECT * FROM purchase_history')
    purchases = cursor.fetchall()

    print("Transaction ID | Product ID | Quantity | Total Price")
    for purchase in purchases:
        print(f"{purchase[0]} | {purchase[1]} | {purchase[2]} | ${purchase[3]:.2f}")

# Function to delete a product by product_id
def delete_product(product_id):
    cursor.execute('''
        DELETE FROM products
        WHERE product_id = ?
    ''', (product_id,))
    conn.commit()
    print(f"Product with ID {product_id} has been deleted.")

# Function to delete a purchase record by transaction_id
def delete_purchase(transaction_id):
    cursor.execute('''
        DELETE FROM purchase_history
        WHERE transaction_id = ?
    ''', (transaction_id,))
    conn.commit()
    print(f"Purchase with transaction ID {transaction_id} has been deleted.")

# Function to delete all products
def delete_all_products():
    cursor.execute('''
        DELETE FROM products
    ''')
    conn.commit()
    print("All products have been deleted.")

# Function to delete all purchases
def delete_all_purchases():
    cursor.execute('''
        DELETE FROM purchase_history
    ''')
    conn.commit()
    print("All purchase history has been deleted.")

# Create the tables
create_tables()

# Add some products
add_product("Water Bottle", 1035, 199)
add_product("Keyboard", 87, 1299)
add_product("Laptop", 100, 50999)
add_product("Key-pad Mobiles", 87, 12999)
add_product("Lcd Display", 17, 12999)
add_product("Headphones", 43, 1999)
add_product("Wireless Mouse", 52, 529)
add_product("Wired Mouse", 20, 250)
add_product("USB-Hub", 20, 950)
add_product("Digital Graphic Tablet", 15, 3960)

# Display products and purchase history before purchase
print("\nBefore Purchase:")
display_products()
show_purchase_history()

# Make a purchase
make_purchase(1, 5)
# delete_all_purchases()
# Display products and purchase history after purchase
print("\nAfter Purchase:")
display_products()
show_purchase_history()



# Close the connection
conn.close()
