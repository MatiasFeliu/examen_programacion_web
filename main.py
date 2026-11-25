from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1")
def ejercicio1():
    return "Ejercicio 1: Compra de pinturas"


@app.route("/ejercicio2")
def ejercicio2():
    return "Ejercicio 2: Inicio de sesión"


if __name__ == "__main__":
    app.run(debug=True)
