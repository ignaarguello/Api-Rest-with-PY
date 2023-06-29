from flask import Flask
from flask_pymongo import PyMongo
import config.database as data_base
from blueprints.products.products_bp import products_bp


app = Flask(__name__)


app.register_blueprint(products_bp)


#* DB Connection
db = data_base.db_connection()


#? Condicional para iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
