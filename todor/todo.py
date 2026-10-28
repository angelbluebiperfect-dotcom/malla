from flask import (Blueprint)
from flask import Flask, render_template,redirect,request
import time
from .modelos.datos_carrera import caja
from .import models
from .import todo_
bp= Blueprint('todo',__name__,url_prefix='/todo')

@bp.route('/register', methods=['GET', 'POST'])
def registre():
  
    if request.method == 'POST':
        user=[]
        academia=[]
        carrera=[]
        datos_carrera=[]
        ramas=[]
        optativa=[]
        consulta1 = request.form.get('consulta1')
        consulta2= request.form.get('consulta2')
        consulta3 = request.form.get('consulta3')
        consulta4= request.form.get('consulta4')
        consulta5= request.form.get('consulta5')
        print(consulta2)
        print(consulta1)
        try:
         academia= todo_.visualiza_academia(consulta1)
        except Exception as e:
            print(f"error en consulta academias {e}")
        try:
            carrera=todo_.visualiza_carrera(consulta2) 
        except Exception as e:
            print(f"error en consulta carreras {e}")
        print(carrera)
        try:
          datos_carrera= todo_.visualiza_datos_carreras(consulta3)
        except Exception as e:
            print(f"error en la consulta datos_carreras {e}")
        try:
            ramas= todo_.visualiza_ramas(consulta4)
        except Exception as e:
            print(f"error en la consulta de ramas {e}")
        try:
            optativa= todo_.visualiza_optativa(consulta5)
        except Exception as e:
            print(f"error en la consulta de optativas {e}")

     
    return render_template('/index.html',texto=consulta1,texto_=consulta2,texto__=consulta3,texto___=consulta4,texto_o=consulta5, academia_=academia,carrera_=carrera,datos_carrera_= datos_carrera,ramas_=ramas,ramas_o=optativa)
@bp.route('/clientes', methods=['GET'])
def index1():
    return  render_template('/clientes.html')
@bp.route('/registra', methods=['GET'])
def register():
    return  render_template('/portafolio/registrar.html')


@bp.route('/loguea')
def loguear():
    return render_template('portafolio/logueo.html')


@bp.route('/')
def inicio():
    return render_template('/index.html')


@bp.route('/list', methods=['GET'])
def _():
    return  "tigres "