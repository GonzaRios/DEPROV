from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarClientes/',views.registrarClientes),
    path('edicionClientes/<ClienteID>', views.edicionClientes),
    path('editarClientes/', views.editarClientes),
    path('eliminarClientes/<ClienteID>', views.eliminarClientes)
    ]