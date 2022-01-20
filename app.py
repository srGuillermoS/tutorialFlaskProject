from crypt import methods

from flask import Flask, render_template
from flask import request
from flask import url_for


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hola mundo"

@app.route('/prueba/')
def prueba():
    id = request.args.get("id")
    return f"Hola Prueba {id}"


@app.route('/prueba2/<int:id>')
@app.route('/prueba2/')
def prueba2(id=None):

    return f"Hola Prueba2 {id}"

#@app.route("/")
#def index():
#    return f"Hola mundo <a href='{url_for('pagina2')}'>pincha aquí</a> "

@app.route('/pagina2/')
def pagina2():
    return "Página2"


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'Hemos accedido con POST'
    else:
        return "Hemos accedido co GET"


@app.route('/info', methods=['GET', 'POST'])
def inicio():
    cad = ""
    cad += "URL:" + request.url + "\n"
    cad += "Metodo:" + request.method + "\n"

    cad += "header:\n"
    for item, value in request.headers.items():
        cad += f"\t{item}:{value}\n"

    cad += "información de formularios (POST):\n"
    for item, value in request.form.items():
        cad += f"\t{item}:{value}\n"

    cad += "información de formularios (GET):\n"
    for item, value in request.args.items():
        cad += f"\t{item}:{value}\n"

    cad += "Ficheros:\n"
    for item, value in request.files.items():
        cad += f"\t{item}:{value}\n"


    return cad


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/template1/")
def template1():
    return render_template("template1.html", nombre="Guillermo", apellido = "Sevilla")

@app.route("/template2/")
def template2():
    data = {'Guillermo':1500, 'José':1000, 'María':1200, 'Ana':2000}
    return render_template("template2.html", data = data)


if __name__ == '__main__':
    app.run(debug=True)

