# Put your app in here
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.get("/add")
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = add(a, b)
    return f"{product}"


@app.get("/sub")
def subtraction():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = sub(a, b)
    return f"{product}"


@app.get("/mult")
def multiplication():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = mult(a, b)
    return f"{product}"


@app.get("/div")
def division():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = div(a, b)
    return f"{product}"


@app.get("/math/<operation>")
def math(operation):
    options = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = options[operation](a, b)
    return f"{product}"
