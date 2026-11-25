from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        precio_tarro = 9000
        total = cantidad * precio_tarro

        if edad < 18:
            porcentaje_descuento = 0
        elif edad <= 30:
            porcentaje_descuento = 0.15
        else:
            porcentaje_descuento = 0.25

        descuento = total * porcentaje_descuento
        total_pagar = total - descuento

        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            total=total,
            descuento=descuento,
            total_pagar=total_pagar
        )

    return render_template("ejercicio1.html")


@app.route("/ejercicio2")
def ejercicio2():
    return "Ejercicio 2: Inicio de sesión"


if __name__ == "__main__":
    app.run(debug=True)
