"""
Basic arithmetic functions: add, subtract, multiply, divide.
"""

# app/calculadora.py


def sumar(a, b):
    """
    Return the sum of two numbers.

    Args:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: a + b
    """
    return a + b


def restar(a, b):
    """
    Return the difference of two numbers.

    Args:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: a - b
    """
    return a - b


def multiplicar(a, b):
    """
    Return the product of two numbers.

    Args:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: a * b
    """
    return a * b


def dividir(a, b):
    """
    Return the division of two numbers.

    Args:
        a (int | float): Numerator.
        b (int | float): Denominator.

    Raises:
        ZeroDivisionError: If b is zero.

    Returns:
        float: a / b
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def potencia(a, b):
    """
    Return a raised to the power of b
    """
    return a**b


def modulo(a, b):
    """
    Return remainder of the division of a by b
    """
    if b == 0:
        raise ZeroDivisionError("Cannot mod by zero")
    return a % b
