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


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render calculator form and process arithmetic operations.

    Handles POST requests with two numbers and an operation:
        - sumar
        - restar
        - multiplicar
        - dividir

    Returns:
        str: Rendered HTML with the result or error message.
    """
    resultado = None
    if request.method == "POST":
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
                resultado = "Invalid operation"
        except ValueError:
            resultado = "Error: Enter valid numbers"
        except ZeroDivisionError:
            resultado = "Error: Cannot divide by zero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(
        debug=True, port=8000, host='0.0.0.0'
    )  # Remove debug=True in production
