from flask import Flask
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
connection = MySQL(app)

@app.route('/cursos')
def get_cursos():
    try:
        return 'OKEY, Aca deberian verse los cursos'
    except Exception as ex:
        return f'Ocurrio un error {ex}'
    

#Funcion para Page Not Found - No olvidarse del ERROR que llega por parametro
def page_not_found(error):
    return '<h1>Error, pagina no encontrada!</h1>'


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
