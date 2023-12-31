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
        db = client["salute_drinks_python"]
        print('● Successful connection to Database ●')
    except ConnectionError:
        print('✖️ Error from connect to database ✖️ ')
    return db
