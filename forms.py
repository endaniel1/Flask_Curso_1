#importamos la clase Form q tiene nuestro archivo wtfoms
#importamos la clase StringField y TextField q tiene nuestro archivo wtfoms
# y importamos la clase EmailField q tiene nuestro archivo wtfoms q tiene la clase wtforms.fields.html5
#Todo esto lo hacemos para crear un formulario html en nuestros archivos html de nuestro proyecto
from wtforms import Form
from wtforms import StringField,TextField
from wtforms.fields.html5 import EmailField

#Aqui se crea una clase y se le pasa la clase Form 
class CommentForm(Form):
	#Despues con StringField() creamos un input tipo texto con el nombres expecificado
	#Con EmailField() creamos un input tipo email con el nombre expecificado
	#Y con TextField() creamos un input tipo text tambien pero q recibira mas texto 
	username = StringField("username")
	email =	EmailField("Correo electronico")
	comment = TextField("Comentario")