# Inventory Management System

## Overview

This is a simple Inventory Management System that allows store owners to manage products and track purchase history. Customers can make purchases, while sellers can update product information. The system uses SQLite as a database and is tracked using Git for version control.

## Features

- Add new products with name, quantity, and price.
- Update the quantity of existing products.
- Make purchases and store them in a purchase history.
- Display all available products.
- Display the purchase history of all transactions.
- Delete individual or all products from the inventory.
- Delete individual or all purchase history records.

## Technologies Used

- Python
- SQLite3
- Git (for version control)

## Installation

1. Clone the repository:
   ```sh
   git clone [repository-url](https://github.com/akshat2111/akshat2111-SE_Lab_2025_A1_01_Repo.git)
   cd inventory-management
   ```
2. Ensure you have Python installed (Python 3 recommended).
3. Run the script:
   ```sh
   python inventory_management.py
   ```

## Usage

- Run the script, and it will automatically create the necessary database tables.
- Modify the script to add products, update quantities, make purchases, and view records.
- Use Git to track changes in the system.

## Example Commands

```python
# Adding a product
add_product("Laptop", 100, 50999)

# Making a purchase
make_purchase(1, 5)

# Display products and purchase history
display_products()
show_purchase_history()

# Delete all products
delete_all_products()
```

## Version Control with Git

- Track changes using Git:
  ```sh
  git add .
  git commit -m "Initial commit with inventory management system"
  git push origin main
  ```

## License

This project is open-source and available for modification and redistribution.

## Team Information

**Team Number:** 10  
**Group:** A1  

### Members:
- **Daniyal Anis** (Roll No: 002311001022)
- **Akshat Verma** (Roll No: 002311001001)
- **Atin Roy** (Roll No: 002311001023)

