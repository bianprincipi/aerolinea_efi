from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empelado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=100) #ej: administrativo, gerente, tecnico
    activo = models.BooleanField(default=True)
    fecha_ingreso = models.DateField()
    es_Administrador = models.BooleanField(default=False)
    es_personal_vuelo = models.BooleanField(default=False) #piloto, copiloto, auxiliar de vuelo, tecnico.. no pasajero comun

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

