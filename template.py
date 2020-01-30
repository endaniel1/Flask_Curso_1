from flask import Flask
from flask import render_template #Aqui importamos render_template en la cual se encarga de importar el html


app = Flask(__name__)

@app.route("/")
def index():
	#Aqui solamente mandamos a retornar a el objeto template q le pasamos el archivo html q tiene el diseño
	return render_template('index.html')

app.run(debug=True,port= '8080')