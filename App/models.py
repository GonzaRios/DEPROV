from django.db import models

# Create your models here.

class Clientes(models.Model):
    ClienteID = models.AutoField(primary_key=True, max_length=6)
    ClienteNombre = models.CharField(max_length=50)
    ClienteApellido = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.ClienteID ,self.ClienteNombre, self.ClienteApellido)