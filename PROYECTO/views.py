from django.http import HttpRequest, HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def curso(request):
    #nombre = "Gonzalo"
    # apellido= "Rios"
    fecha= datetime.datetime.now()
    # arch = open("C:/Users/gonzalo.rios/AppData/Local/Programs/Python/Python39/Scripts/PROYECTO/TEMPLATES/plantilla.html")
    # plt = Template(arch.read())
    # arch.close()
    # ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido,"now":fecha})
    # documento = plt.render(ctx)
    return render(request, "gestionClientes.html", {"now":fecha})

