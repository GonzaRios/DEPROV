from pydoc import cli
from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.

def home(request):
    clienteLista = Clientes.objects.all()
    return render(request, "gestionClientes.html", {"clientes": clienteLista})
    
def registrarClientes(request):
    ID = request.POST['txtID']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']

    clientes = Clientes.objects.create(
        ClienteID=ID, ClienteNombre=nombre, ClienteApellido=apellido)
    return redirect('/')

def edicionClientes(request, ClienteID):
    cliente = Clientes.objects.get(ClienteID=ClienteID)
    return render(request, "edicionClientes.html", {"cliente": cliente})

def editarClientes(request):
    ID = request.POST['txtID']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']

    cliente = Clientes.objects.get(ClienteID=ID, ClienteNombre=nombre, ClienteApellido=apellido)
    cliente.ClienteID = ID
    cliente.ClienteNombre = nombre
    cliente.ClienteApellido = apellido
    cliente.save()  
    
    return redirect('/')

def eliminarClientes(request, ClienteID):
    cliente = Clientes.objects.get(ClienteID=ClienteID)
    cliente.delete()

    return redirect('/')