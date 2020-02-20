#importamos la clase Form q tiene nuestro archivo wtfoms
#importamos la clase StringField y TextField q tiene nuestro archivo wtfoms
# y importamos la clase EmailField q tiene nuestro archivo wtfoms q tiene la clase wtforms.fields.html5
#Todo esto lo hacemos para crear un formulario html en nuestros archivos html de nuestro proyecto
from wtforms import Form 
from wtforms import StringField,TextField #Para input de tipo Text
from wtforms.fields.html5 import EmailField #Para input de tipo Email
from wtforms import HiddenField #Para input de tipo Hidden
from wtforms import PasswordField #Para input de tipo Password

from models import User #Aqui tenemos q importar el modelo User para hacer consultas antes de hacer los registros

#Aqui importamos la clase validators q tiene nuestros archivo wtforms, en la cual se va a encargar de las validaciones
from wtforms import validators

#Resive un Formulario y un campo
def length_honeypot(form,field):
	if len(field.data)>0:
		raise validators.ValidationError("El Campo Debe Estar Vacio!.")


#Aqui se crea una clase y se le pasa la clase Form 
class CommentForm(Form):	
	#Y con TextField() creamos un input tipo text tambien pero q recibira mas texto 	
	comment = TextField("Comentario",[
				validators.length(min=3,message="Ingrese Un Comentario Mas Largo!.")
			])
	#este es para un campo de texto oculto
	honeypot=HiddenField("",[
				length_honeypot
			])

#Esta clase crea los input de nuestro login
class LoginForm(Form):
	#Despues con StringField() creamos un input tipo texto con el nombres expecificado
	#Con EmailField() creamos un input tipo email con el nombre expecificado
	#Como sengundo parametro le indicamos las validaciones q queremos
	#En este caso por medio de un lista mandamos a llamar a los metodos o clases correspondiente a las misma
	username = StringField("Username",[
					validators.Required(message="El Username Es Requerido!."),
					validators.length(min=4,max=25,message="Ingrese Un Username Valido!.")
				])
	password=PasswordField("Password",[
				validators.Required(message="El Password Es Requerido!.")
			])
		
#Esta clase para crear el formario de creacion de usuario
class CreateUser(Form):
	username = StringField("Username",[
					validators.Required(message="El Username Es Requerido!."),
					validators.length(min=4,max=25,message="Ingrese Un Username Valido!.")
				])
	email =	EmailField("Correo electronico",[
				validators.Required(message="El Email Es Requerido!."),
				validators.Email(message="Ingrese Un Email Valido")
			])
	password=PasswordField("Contraseña",[
				validators.Required(message="El Password Es Requerido!.")
			])
	#Aqui se crea este metodo a partir de los q vamos a hacer con los datos enviado en nuestro formulario
	#lo q recivemos es el formulario y el campo de texto(obligatorio para q funcione)
	def validate_username(form,field):
		username=field.data#Aqui otenemos los datos del username del formulario
		user=User.query.filter_by(username=username).first()#consultamos aqui si existe en la base de dato
		if user is not None:#comprobamos si no existe y si existe le mandomos este mensaje o excepcion 
			raise validators.ValidationError("El Username Se Encuentra en Uso!.")