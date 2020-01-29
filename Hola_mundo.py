from flask import Flask


app = Flask(__name__)#Aqui se hace una instancia o nuevo objeto 

#Osea aqui en pocas palablas la ruta raiz ejecuta la funcion hello
@app.route("/")#Aqui un decorador para en el cual se va a manejar nuestras rutas
def hello():#AQUI UNA FUNCION SENCILLA Q DEVUELVE UN STRING
    return "Hello, World!"

app.run()#Aqui se encarga de ejecutar el servidor el metodo run()