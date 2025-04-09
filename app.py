from flask import Flask,url_for

app = Flask(__name__)

@app.route("/")
def principal():
    url_hola = url_for("hello")
    url_dado = url_for("dado",caras=6)
    url_logo = url_for("static",filename="img/duki.png")
    
    return """
     <a href= '/hola'>:)</a>" 
     <a href= '/chau'>:(</a>"
    <br>
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">chau</a>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar dado</a>
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


def main():
  url_hola = url_for("hello")
  url_dado = url_for("dado",caras=6)
  url_logo = url_for("static",filename="img/duki.png")
 
  return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">chau</a>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar dado</a>
 """
