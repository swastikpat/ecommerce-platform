
# File: search_api_optimization.py
# Optimized Product Search API

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('ecommerce.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/search', methods=['GET'])
def search_products():
    category = request.args.get('category')
    min_price = request.args.get('min_price', 0)
    max_price = request.args.get('max_price', float('inf'))
    sort_order = request.args.get('sort', 'asc')
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 20))
    offset = (page - 1) * size

    query = """
        SELECT * FROM products
        WHERE category = ? AND price BETWEEN ? AND ?
        ORDER BY price {sort}
        LIMIT ? OFFSET ?
    """.format(sort="ASC" if sort_order == "asc" else "DESC")

    params = (category, min_price, max_price, size, offset)
    conn = get_db_connection()
    products = conn.execute(query, params).fetchall()
    conn.close()

    return jsonify([dict(product) for product in products])

if __name__ == '__main__':
    app.run(debug=True)
