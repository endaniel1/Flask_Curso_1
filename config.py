import os #Aqui importamos para trabajar con variables globales 
#Aqui se crea esta clase de configuracion  
#En el cual va a tener la clave secreta de nuestro proyecto
class Config(object):
	SECRET_KEY = 'Enrique'
	#Aqui estas son las configuraciones para q interprete el envio de correo 
	#Pero el asunto esta q nose porque no lo hagara nose q ay q configurar para q funciones bn o descarge algo mal
	#Esta todo como dice la documentacion pero nose si es por el MAIL_USERNAME o MAIL_PASSWORD
	MAIL_SERVER="smtp.gmail.com"
	MAIL_PORT=465
	MAIL_USE_SSL=False
	MAIL_USE_TLS=True
	MAIL_USERNAME="enriq_1997@hotmail.com"
	MAIL_PASSWORD=os.environ.get("PASSWORD_EMAIL_CF")


#Aqui despues hacemos otra clase en la cual va a tener todas la configuraciones para nuestro aplicacion en desarrollo
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/flask_1"
	SQLALCHEMY_TRACK_MODIFICATIONS=False
		
		