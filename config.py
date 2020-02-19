import os #Aqui importamos para trabajar con variables globales 
#Aqui se crea esta clase de configuracion  
#En el cual va a tener la clave secreta de nuestro proyecto
class Config(object):
	SECRET_KEY = 'Enrique'
#Aqui despues hacemos otra clase en la cual va a tener todas la configuraciones para nuestro aplicacion en desarrollo
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/flask_1"
	SQLALCHEMY_TRACK_MODIFICATIONS=False
		
		