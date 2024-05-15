from flask import Blueprint, redirect, url_for, render_template 
from models.Cliente import Cliente
from views import show_tasks, show_add_task_form, show_delete_task_form

from models.Cliente import *

app = Flask(__name__)


@app.route('/registrarCliente', methods=['POST'])
def registrarCliente():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    cliente = registrarCliente(nombre, direccion, telefono)

def consultarCliente(cliente):
    nombre = cliente.getNombre()
    direccion = cliente.getDireccion()
    telefono = cliente.getTelefono()

    return nombre, direccion, telefono # Devolver la información consultada

def modificarCliente(cliente, nombre, direccion, telefono):
    cliente.setNombre(nombre)
    cliente.setDireccion(direccion)
    cliente.setTelefono(telefono)

