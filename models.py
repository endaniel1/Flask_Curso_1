from flask_sqlalchemy import SQLAlchemy #Aqui importamos la clase flask_sqlalchemy

import datetime #Aqui importamos la clase para tener el tiempo
from flask_bcrypt import Bcrypt #Aqui importamos la clase para tener la encriptacion

db=SQLAlchemy()#Aqui creamos una instancia de la clase SQLAlchemy
bcrypt = Bcrypt()#Aqui creamos una instancia para encriptar cosan con bcrypt

#Aqui creamos una clase en la cual va a tener el modelo a crear en nuestra base de datos
class User(db.Model):
	#Aqui le decimos a q tabla 
	__tablename__="Users"
	#Y aqui sencillamente creamos los datos q va a tener nuestra tabla
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(50),unique=True)
	email=db.Column(db.String(40))
	password=db.Column(db.String(66))
	created_date=db.Column(db.DateTime,default=datetime.datetime.now)

	#Aqui iniciamos nuestro construtor para q tenga los datos
	def __init__(self, username, password, email):
		self.username=username
		self.password=self.__create_passwoord(password)
		self.email=email
	#Aqui creamos este metodo para encriptar contraseñña
	def __create_passwoord(self, secret):
		return bcrypt.generate_password_hash(secret)
	#Aqui creamos otro metodo para verificar la contraseña encriptada
	def verify_password(self, secret):
		return bcrypt.check_password_hash(self.password,secret)