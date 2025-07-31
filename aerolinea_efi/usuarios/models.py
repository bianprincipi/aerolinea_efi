from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_ingreso = models.DateField()
    es_administrador = models.BooleanField(default=False)
    es_personal_vuelo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"
