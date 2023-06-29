from email import message
from flask import Blueprint, jsonify, request
from config.database import db_connection
from models.product_model_data import Product

products_bp = Blueprint("products", __name__)

db = db_connection()


# ? Routes for Products
@products_bp.route("/products")
def get_products():
    products = db['products']
    productsReceived = products.find()
    return productsReceived


@products_bp.route('/products', methods=['POST'])
def create_product():
    try:
        products = db['products']

        name = request.json['name']
        price = request.json['price']
        quantity = request.json['quantity']

        if name and price and quantity:
            product = Product(name, price, quantity)
            products.insert_one(product.toDBCollection())
        else:
            return jsonify({
                "error_message": "Please complete the required fields",
            })

        return jsonify({
            "message": f"Product created successfully - {name}"
        })

    except Exception as e:
        print("Error:", str(e))
