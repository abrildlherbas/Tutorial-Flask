from flask import Flask,url_for,render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def principal():
    url_hola = url_for("saludar")
    #url_dado = url_for("dado",caras=6)
    url_logo = url_for("static",filename="img/duki.png")
    
    return """
     <a href= '/hola'>:)</a>" 
     <a href= '/chau'>:(</a>"
    <br>
    <a href="{/hola}">Hola</a>
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


 
db=None

def abrirConexion():
 global db
 db = sqlite3.connect("instance/datos.sqlite")
 db.row_factory = sqlite3.Row
 return db

def cerrarConexion():
 global db
 if db is not None:
    db.close()
    db = None

@app.route("/usuarios/")
def obterGente():
   global db 
   conexion = abrirConexion()
   cursor = conexion.cursor()
   cursor.execute ('SELECT * FROM usuarios')
   resultado = cursor.fetchall()
   cerrarConexion()
   fila = [dict(row) for row in resultado]
   return str(fila) 
 

#ruta para borrar un id 
@app.route("/borrar/<int:id>")
def borrar (id):
   abrirConexion()
   db.execute("DELETE FROM usuarios WHERE id=2" , (usr,))
   db.commit()
   cerrarConexion()

#ruta para insertar un usuario y email
@app.route("/insertar/<string:usuario>/<string:email>")
def insertar (usuario,email):
   abrirConexion()
   db.execute("INSERT INTO usuarios (usuario,email) VALUES (?, ?);", (usuario,email))
   db.commit()
   cerrarConexion()

#ruta para mostrar nombre,email del usuario
@app.route("/mostrar/<int:id>")
def mostrar(id):
   abrirConexion() #abre la conexion con la base de datos 
   cursor = db.cursor()
   cursor.execute("SELECT usuario, email FROM usuarios WHERE id=?", (id,))
   res = cursor.fetchone() #res es una variable, obtiene el resultado de la consulta                 
   cerrarConexion() #cierra la conexion con la base de datos
   return f"nombre: {res['usuario']}, email del usuario: {res['email']}"

#ruta para cambiar el email del usuario
@app.route("/cambiar/<string:usuario>/<string:nuevo_email>")
def testUpdate (usuario,nuevo_email):
   abrirConexion()
   cursor = conexion.cursor()
   cursor.execute = ("SELECT email FROM usuarios WHERE usuarios=?", (usuario,))
   res = cursor.fetchone()
   db.commit()
   cerrarConexion()

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT id,usuario,email,telefono,direccion FROM usuarios WHERE id = ?; ", (id,))
   res = cursor.fetchone()
   cerrarConexion()
   usuario = None
   email = None 
   telefono = None
   direccion = None
   if res != None:
    usuario=res['usuario']
    email=res['email']
    telefono=res['telefono']
    direccion=res['direccion']
   return render_template("datos.html", id=id, usuario=usuario, email=email, telefono=telefono, 
   direccion=direccion)