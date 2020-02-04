from flask import Flask 
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect #Aqui esta es para tener un token o Csrf para nuestros formularios

from flask import flash #Aqui para los mensajes 

from flask import g #Aqui para utilizar variable de tipo global

from flask import url_for #Aqui esta es para solo decirle a q url se quiere q vayamos
from flask import redirect #Aqui con esta es para redireccionarnos a un lugar

from flask import session #Aqui para el manejo de sessiones

from flask import make_response #Este es para los cookies

import forms #Aqui importamos el archivo forms.py de nuestro proyecto
import json #Aqui para trabajar con formato Json


app = Flask(__name__)
app.secret_key = "Enrique" #Aqui creamos una clave secreta para nuestra aplicacion puede ser cualquiera

csrf=CsrfProtect(app)#Y aqui le decimos q nuestros csrft eeste en nuestra aplicacion

#Aqui con el decorrador errorhandler() va a ser el q nos indentifique los errores en este caso el 404
@app.errorhandler(404)
def page_not_found(error): #Esta funcion resive como parametro un error
	#Aqui sencillamente retornamos a una html sencillo y despues le pasamos y eh indicamos a python el tipo de error q ocurrio
	return render_template("404.html"),404


#Aqui sencillamente esta funcion se va a ejecutar siempre oosea de primer lugar antes q se ejecute otra funcion
@app.before_request
def before_request():
	g.test=[1,2,3,4]
	if "username" not in session:#Aqui sencillamente valido si no existe la variable de session
		#print(request.endpoint)
		print("El Usuario Nesecita Login!")

@app.route("/")
def index():
	print(g.test)
	if "username" in session: 
		username=session["username"]
		#print(username)
	title="Curso Flask| Bienvenido"
	return render_template("index.html",title=title)

#Este funcion se va a ejecutar al final o despues q se ejecute la funciones q comparte la vista
@app.after_request
def after_request(response):
	print(g.test)
	return response #Aqui siempre se va a devolver algo para q funcione esta funcion

#Aqui funcion para crear un comentario
@app.route('/comment',methods=["GET","POST"])
def comment():

	#Aqui creamos una varible q tenga nuestros cookie
	#Con request.cookies.get() indicamos q tenga a los cookies
	#Le pasamos como parametros el nombre del cookie y como sengundo si no existe q diga q no existe
	custome_cookie=request.cookies.get("custome_cookie","No Existe Esta Cookie")
	print(custome_cookie)#Aqui mandamos a imprimir nuestro valor de nuestros cookie

	#Aqui llamaos a la clase forms.CommentForm() q tiene nuestro archivo
	#Ahora si nuestra tambien si viene algun tipo de tados creamos una instancia con eso tipo de datos
	#Para luego verlos en nuestros inputs
	comment_form=forms.CommentForm(request.form)
	
	#Aqui sencillamente lo q se hace es q si el method es Post mostramos los datos nuestro formulario
	if request.method=="POST" and comment_form.validate():
		print (comment_form.username.data)
		print (comment_form.email.data)
		print (comment_form.comment.data)
	else:
		print("Error En El Formulario!.")
	title="Curso Flask| Formulario De Comentarios"
	return render_template("comment.html",title=title,form=comment_form)

#Aqui la ruta del login
@app.route('/login',methods=["GET","POST"])
def login():
	login_form=forms.LoginForm(request.form) #Aqui llamamos a nuestra clase LoginForm() de nuestro archivo forms
	title="Curso Flask| Formulario Login"

	if request.method == "POST" and login_form.validate():
		username=login_form.username.data #Aqui lo q hago es tener los datos del usuario
		success_message="Bienvenido {}".format(username) #Aqui creamos un mensaje
		flash(success_message)#Aqui con la clase flash() le pasamos el mensaje para q lo muestre

		session["username"]=login_form.username.data #Aqui sencillamente creamos uan varible de seccion llamada username

	return render_template("login.html",title=title,form=login_form)

#Aqui esta es la ruta para cerrar seccion
@app.route('/logout')
def logout():
	if "username" in session:
		session.pop("username")#Con session.pop() destruimos las variables de secciones q queremos
	#Aqui retornamos con la clase redirect a la url correspondiente
	#Esto lo hacemos con la clase url_for() q le expecificamos a cual vamos a ir
	return redirect(url_for("login"))

#Aqui la ruta para crear un cookie
@app.route('/cookie')
def cookie():
	#Aqui creamos una variable en el cual vamos a crear nuestros cookie
	#Sencillamente con make_response() crearemos nuestrso cookie en este caso de nuestra vista "cookie.html"
	#Luego con la clase reponse.set_cookie() obtenemos nuestro cookie para darle u nombre y valor para mostrar
	reponse=make_response(render_template("cookie.html"))
	reponse.set_cookie("custome_cookie","Enrique")
	return reponse #Aqui sencillamente retornamos nuestra vista q ya es un cookie

#Aqui la ruta de forma de Ajax para el login
@app.route('/ajax-login',methods=["POST"])
def ajax_login():
	print(request.form)#Aqui mostramos mlos datos q trae el formulario
	username=request.form["username"]#Obtengo lso datos del username
	response={
		"status":400,
		"username":username,
		"id":1
	}
	return json.dumps(response)#Aqui retorno en formato json los datos con la clase json.dumps()

if __name__=='__main__':
	app.run(debug=True,port=8080)