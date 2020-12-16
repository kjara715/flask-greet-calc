from flask import Flask, request
from operations import add, sub, mult, div
app=Flask(__name__)

@app.route('/add')
def add_up():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    sum = add(a, b)
    return str(sum)

@app.route('/sub')
def sub_tract():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    subtract= sub(a,b)
    return str(subtract)
@app.route('/mult')
def mult_iply():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    multiplied= mult(a, b)
    return str(multiplied)
@app.route('/div')
def div_ide():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    divided= div(a, b)
    return str(divided)


math_equations={
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
@app.route('/math/<operation>')
def calculate(operation):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=math_equations[operation](a,b)
    return str(result)