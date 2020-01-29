from flask import Flask
from flask import request #Aqui con esta importacion lo q se hace es para resivir variables de entorno

app = Flask(__name__)

@app.route("/")
def index():
    return "Aqui cambio algunas cosas, otra vez"

#Aqui lo q hicimos fue crear una nueva ruta en nuestra aplicacion
@app.route("/saluda")
def hello():#Q aqui ejecuta la funcion
    return "Aqui van otros mensaje!"

#Aqui creamos otra ruta en la cual resivira parametros
@app.route("/parametros")
def parametros():
	#Aqui sencillamente recibira los parametros q viene tipo get()
	#en la cual decimos por medio de una varible q reciva un parametro y en su defecto q imprima "q no tiene nada"
	#Esto lo hacemos con el metodo .args.get() q tiene la clase request 
	param=request.args.get("params1","no contiene parametros")
	param2=request.args.get("params2","no contiene parametros")
	#Aqui sencillamente le damos formatos a nuestras variables y devolvemos nuestro string
	return "El parametro es: {} , {}".format(param,param2)

#Aqui le pasamos debug=True lo q indica es q lo q hagamos en tiempo de ejecucion no tengamos q reiniciar el servidor sino q los 
#Cambios se ven cuando recargamos la pagina
#Lo siguiente es q con port=8080 lo q se hace es cambiar a el nombre del puerte q se quiere q inicie nuestra aplicacion  	    
app.run(debug=True,port= '8080')