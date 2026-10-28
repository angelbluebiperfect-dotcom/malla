from flask import Flask, render_template
from . import models

def elabora():
  models.ejecuta()
def create_app():

 app= Flask(__name__)
 
 #Configuracion proyecto

 app.config.from_mapping(
    DEBUG= True,
    SECRETE_KEY='dev'
 ) 


 #Registrar blueprint
 from . import todo
 app.register_blueprint(todo.bp)
 
 @app.route('/')
 def index():
    return render_template("index.html")

 return app