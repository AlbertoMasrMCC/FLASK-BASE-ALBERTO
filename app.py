from flask import Flask
from traducir import traducir_ingles_espanol

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"

@app.route("/traducir/<texto>")
def traducir(texto):
    return traducir_ingles_espanol(texto)

@app.route("/about")
def about():
    return "<h1>Esta es la pagina de about</h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)