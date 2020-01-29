from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route("/")
def index():
    return "Aqui cambio algunas cosas, otra vez"

@app.route("/parametros")
@app.route("/parametros/<name>/<int:num>")
def parametros(name="Este es un valor por default",num="nada"):
	return "El parametro es: {}, {}".format(name,num)

   	    
app.run(debug=True,port= '8080')