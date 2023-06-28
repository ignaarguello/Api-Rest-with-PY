from pymongo import MongoClient
import certifi
import dotenv
import os

dotenv.load_dotenv()

MONGO_URI = os.getenv('URL_DATA_BASE')
certified = certifi.where()


def db_connection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=certified)
        db = client("Salute Drinks Python")
    except ConnectionError:
        print('Error en la ejecucion de la base de datos')
    return db
