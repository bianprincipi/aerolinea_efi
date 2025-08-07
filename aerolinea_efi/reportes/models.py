from django.db import models
from vuelos.models import Vuelo
from datetime import datetime

class ReportePasajerosPorVuelo(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    generado_por = models.CharField(max_length=100)
    fecha_generacion = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Reporte de vuelo {self.vuelo} - {self.fecha_generacion.date()}"