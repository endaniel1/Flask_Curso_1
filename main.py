from flask import Flask 
from flask import render_template

import forms #Aqui importamos el archivo forms.py de nuestro proyecto

app = Flask(__name__)

@app.route('/')
def index():
	comment_form=forms.CommentForm()#Aqui llamaos a la clase forms.CommentForm() q tiene nuestro archivo
	title="Curso Flask"
	return render_template("index.html",title=title,form=comment_form)

if __name__=='__main__':
	app.run(debug=True,port=8080)