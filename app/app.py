# app/app.py
"""
Flask web app for a simple calculator.

Routes:
    / : Display the calculator form and handle operations
    (add, subtract, multiply, divide).
"""
from flask import Flask, render_template, request
from app.calculator import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Render the calculator form.

    Returns:
        str: Rendered HTML with the calculator form.
    """
    return render_template("index.html", resultado=None)


@app.route("/", methods=["POST"])
def calculate():
    """
    Process arithmetic operations and re-render the form with results.

    Handles POST requests with two numbers and an operation:
        - sumar
        - restar
        - multiplicar
        - dividir

    Returns:
        str: Rendered HTML with the result or error message.
    """
    resultado = None
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacion = request.form["operacion"]

        if operacion == "sumar":
            resultado = sumar(num1, num2)
        elif operacion == "restar":
            resultado = restar(num1, num2)
        elif operacion == "multiplicar":
            resultado = multiplicar(num1, num2)
        elif operacion == "dividir":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operación no válida"
    except ValueError:
        resultado = "Error: Introduce números válidos"
    except ZeroDivisionError:
        resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":  # pragma: no cover
    app.run(port=8000, host="0.0.0.0")
