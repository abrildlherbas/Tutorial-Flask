from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
     <a href= '/hola'>:)</a>" 
     <a href= '/chau'>:(</a>" 
     """

@app.route("/hola")
def saludar():
    return f"<h2>hello!</h2>"

@app.route("/hola/<string:nombre>")
def saludar_con_nombre(nombre):
    return f"<h2>hello,{nombre}!</h2>"

@app.route("/chau")
def despedir():
    return "<h2>chau</h2>"

