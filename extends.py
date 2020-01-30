from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index(name="Enrique"):
	return render_template('index.html',nombre=name)

@app.route("/cliente")
def cliente():
	my_lista=["test1","test2","test3","test4","test5"]
	return render_template('cliente.html',my_lista=my_lista)

app.run(debug=True,port= '8080')