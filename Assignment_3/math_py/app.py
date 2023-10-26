from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

#add other routes here
# Definisco la rotta
@app.route('/sub')
# Definisco la funzione e ciò che deve fare
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        # Serve per ottenere un oggetto di risposta
        return make_response(jsonify(s=a-b), 200)
    else:
        return make_response('Invalid input\n', 400)
    
# Definisco la rotta
@app.route('\mul')
#Definisco la funzione
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a*b), 200)
    else:
        return make_response('Invalid Input', 400)

# Definisco la rotta
@app.route('\div')
#Definisco la funzione
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a/b), 200)
    else:
        return make_response('Invalid Input', 400)

# Definisco la rotta
@app.route('\mod')
#Definisco la funzione
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a%b), 200)
    else:
        return make_response('Invalid Input', 400)

def create_app():
    return app