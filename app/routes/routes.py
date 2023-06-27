from app import app

@app.route('/')
def hello():
    return 'Mi Primera app con flask perri'


@app.route('/products')
def helloo():
    return 'Productos disponibles'


if __name__ == '__main__':
    app.run()
