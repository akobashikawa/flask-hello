"""
Simple flask app
"""
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """ root """
    # return '<p>Index page</p>'
    return render_template('index.html')

@app.route('/helloworld')
def helloworld():
    """ hello world """
    # return '<p>Hello World</p>'
    return render_template('helloworld.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='Anonymous'):
    """ hello name """
    # return f"<p>Hello {name}</p>"
    return render_template("hello.html", name=name)

@app.route('/contacto/')
def contacto():
    """ presenta formulario de contacto """
    return render_template("contacto.html")

@app.route("/enviar-formulario", methods=['POST'])
def enviar_formulario():
    """ procesa formulario """
    nombre = request.form['nombre'];
    email = request.form['email'];
    mensaje = request.form['mensaje'];
    return render_template("saludo.html", nombre = nombre, email = email, mensaje = mensaje)

@app.route("/api/enviar-formulario", methods=['POST'])
def api_enviar_formulario():
    """ procesa formulario """
    nombre = request.json['nombre'];
    email = request.json['email'];
    mensaje = request.json['mensaje'];
    return jsonify({'nombre': nombre, 'email': email, 'mensaje': mensaje})
