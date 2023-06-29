from flask import Blueprint

products_bp = Blueprint("products", __name__)

@products_bp.route("/products")
def hello():
    return 'Probando los putos blueprints'