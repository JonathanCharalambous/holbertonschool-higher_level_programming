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

@app.route('/products')
def data():
    source = request.args.get('source')
    record_id = request.args.get('id')

    data_list = []

    if source == 'json':
        try:
            with open('products.json') as f:
                data_list = json.load(f)
        except Exception as e:
            return f"Error loading JSON: {e}", 500

    elif source == 'csv':
        try:
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                data_list = list(reader)
        except Exception as e:
            return f"Error loading CSV: {e}", 500

    else:
        return "Wrong source"
    
    if record_id:
        data_list = [item for item in data_list if str(item.get("id")) == str(record_id)]
        if not data_list:
            return "Product not found"
    return render_template("product_display.html", products=data_list)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)