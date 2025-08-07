from django.db import models
from vuelos.models import Vuelo
from pasajeros.models import Pasajero
from aviones.models import Asiento

class Reserva(models.Model):
    ESTADOS = [
        ('Activa', 'Activa'),
        ('Cancelada', 'Cancelada'),
        ('Completada', 'Completada')
    ]

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    asiento = models.OneToOneField(Asiento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_reserva = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.pasajero.nombre}"


class Boleto(models.Model):
    ESTADOS = [
        ('Vigente', 'Vigente'),
        ('Usado', 'Usado'),
        ('Cancelado', 'Cancelado')
    ]

    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=100)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __str__(self):
        return f"Boleto - {self.reserva.codigo_reserva}"