from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            item_data = json.load(file)
        items_data = item_data.get('items', [])
    except:
        items_data = []
    
    return render_template('items.html', items=items_data)

@app.route('/products')
def display_products():
    source = request.args.get('source') 
    product_id = request.args.get('id')
    
    if source not in ('json', 'csv'):
        return render_template('product_display.html', error="Wrong source")
    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    
    if product_id:
        try:
            product_id = int(product_id)
            products_filtered = [p for p in products if p['id'] == product_id]
            if products_filtered:
                products = products_filtered
            else: 
                return render_template('product_display.html', error="Product not found.")
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format. Must be numeric.")
    
    return render_template('product_display.html', products=products)


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

if __name__ == '__main__':
    app.run(debug=True, port=5000)