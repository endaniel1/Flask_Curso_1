#importamos la clase Form q tiene nuestro archivo wtfoms
#importamos la clase StringField y TextField q tiene nuestro archivo wtfoms
# y importamos la clase EmailField q tiene nuestro archivo wtfoms q tiene la clase wtforms.fields.html5
#Todo esto lo hacemos para crear un formulario html en nuestros archivos html de nuestro proyecto
from wtforms import Form 
from wtforms import StringField,TextField #Para input de tipo Text
from wtforms.fields.html5 import EmailField #Para input de tipo Email
from wtforms import HiddenField #Para input de tipo Hidden
from wtforms import PasswordField #Para input de tipo Password


#Aqui importamos la clase validators q tiene nuestros archivo wtforms, en la cual se va a encargar de las validaciones
from wtforms import validators

#Resive un Formulario y un campo
def length_honeypot(form,field):
	if len(field.data)>0:
		raise validators.ValidationError("El Campo Debe Estar Vacio!.")


#Aqui se crea una clase y se le pasa la clase Form 
class CommentForm(Form):
	#Despues con StringField() creamos un input tipo texto con el nombres expecificado
	#Con EmailField() creamos un input tipo email con el nombre expecificado
	#Y con TextField() creamos un input tipo text tambien pero q recibira mas texto 
	#Como sengundo parametro le indicamos las validaciones q queremos
	#En este caso por medio de un lista mandamos a llamar a los metodos o clases correspondiente a las misma
	username = StringField("username",[
					validators.Required(message="El Username Es Requerido!."),
					validators.length(min=4,max=25,message="Ingrese Un Username Valido!.")
				])
	email =	EmailField("Correo electronico",[
				validators.Required(message="El Email Es Requerido!."),
				validators.Email(message="Ingrese Un Email Valido")
			])
	comment = TextField("Comentario")
	honeypot=HiddenField("",[
				length_honeypot
			])

#Esta clase crea los input de nuestro login
class LoginForm(Form):
	username = StringField("Username",[
					validators.Required(message="El Username Es Requerido!."),
					validators.length(min=4,max=25,message="Ingrese Un Username Valido!.")
				])
	password=PasswordField("Password",[
				validators.Required(message="El Password Es Requerido!.")
			])
		

