from flask import Flask
from flask import request #Aqui con esta importacion lo q se hace es para resivir variables de entorno

app = Flask(__name__)

@app.route("/")
def index():
    return "Aqui cambio algunas cosas, otra vez"

@app.route("/parametros")
#Aqui sencillamente lo q hacemos con <name> se le indica q va a recivir una variable
#Luego con <int:num> lo q hace es decir q solamente reciva una varible tipo entera para q sea valida la url
@app.route("/parametros/<name>/<int:num>")
def parametros(name="Este es un valor por default",num="nada"):
	return "El parametro es: {}, {}".format(name,num)

   	    
app.run(debug=True,port= '8080')