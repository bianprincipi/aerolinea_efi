from django.db import models
from aviones.models import Avion
from datetime import timedelta

class Vuelo(models.Model):
    ESTADOS = [
        ('Programado', 'Programado'),
        ('En vuelo', 'En vuelo'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    ]

    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    duracion = models.DurationField(default=timedelta(0))
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Programado')
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origen} - {self.destino} ({self.fecha_salida})"
