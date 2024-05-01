from flask import Blueprint, redirect, url_for, render_template 
from models.cocinero import Cocinero
from views import show_tasks, show_add_task_form, show_delete_task_form

from models.cocinero import *

app = Flask(__name__)


@app.route('/registrarCocinero', methods=['POST'])
def registrarCocinero():
    nombre = request.form['nombre']
    estacion = request.form['estacion']
    salario = request.form['salario']
    cocinero = crearCocinero(nombre, salario, estacion)

def consultarCocinero(cocinero):
    nombre = cocinero.getName()
    salario = cocinero.getSalary()
    estacion = cocinero.getEstacion()

    return nombre, salario, estacion  # Devolver la información consultada

def modificarCocinero(cocinero, nombre, salario, estacion):
    cocinero.setName(nombre)
    cocinero.setSalary(salario)
    cocinero.setEstacion(estacion)



