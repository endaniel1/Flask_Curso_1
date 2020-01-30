from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/user/<name>")
def index(name="Enrique"):
	#Aqui creamos una variables para mostrar en las vista
	ano=15 
	my_lista=[1,2,3,4,5,6,7,8,9]
	#Aqui retornamos la vista html y como parametros adicionales le pasamos las variables q queremos
	return render_template('user.html',nombre=name,ano=ano,my_lista=my_lista)

app.run(debug=True,port= '8080')