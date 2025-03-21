from flask import Flask, render_template, request
import sqlite3
import json
import csv
import os

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

def load_json_data():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_csv_data():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, KeyError, ValueError):
        return []

def load_sql_data():
    """Load product data from SQLite database"""
    products = []
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Execute query to fetch all products
        cursor.execute('''SELECT id, name, category, price FROM products''')
        rows = cursor.fetchall()
        
        # Convert rows to dictionary format
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': float(row[3])
            }
            products.append(product)
            
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {str(e)}")
        return []
        
    finally:
        if conn:
            conn.close()
            
    return products

@app.route('/products')
def display_products():
    """Display products from multiple data sources"""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if not source:
        return render_template('product_display.html', 
                             error="Source parameter is required (json, csv, or sql)")
    
    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', 
                             error="Invalid source. Use 'json', 'csv', or 'sql'")
    
    try:
        # Load data based on source
        if source == 'json':
            products = load_json_data()
        elif source == 'csv':
            products = load_csv_data()
        elif source == 'sql':
            products = load_sql_data()
        
        if not products:
            return render_template('product_display.html',
                                error=f"No products found in {source} source")
        
        # Filter by product ID if provided
        if product_id:
            try:
                product_id = int(product_id)
                products_filtered = [p for p in products if p['id'] == product_id]
                if products_filtered:
                    products = products_filtered
                else:
                    return render_template('product_display.html',
                                        error="Product not found")
            except ValueError:
                return render_template('product_display.html',
                                    error="Invalid ID format. Must be numeric")
        
        return render_template('product_display.html', products=products)
        
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return render_template('product_display.html',
                             error="An error occurred while processing your request")

def init_db():
    """Initialize the SQLite database with sample data"""
    conn = None
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Create products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # Insert sample data
        sample_data = [
            (1, 'Laptop', 'Electronics', 999.99),
            (2, 'Headphones', 'Electronics', 99.99),
            (3, 'Coffee Maker', 'Appliances', 49.99)
        ]
        
        cursor.executemany('''
            INSERT OR REPLACE INTO products (id, name, category, price)
            VALUES (?, ?, ?, ?)
        ''', sample_data)
        
        conn.commit()
        
    except sqlite3.Error as e:
        app.logger.error(f"Database initialization error: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Initialize database before running the app
    init_db()
    app.run(debug=True, port=5000)