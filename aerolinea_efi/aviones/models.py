from django.db import models

# Create your models here.

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    filas = models.IntegerField()
    columnas = models.IntegerField()

    def __str__(self):
        return self.modelo

class Vuelo(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()
    fehca_llegada = models.DateTimeField()
    duracion = models.DurationField(null= True, blank= True)

    ESTADOS = [
        ('activo', 'Activo'),
        ('cancelado', 'Cancelado'),
        ('retrasado', 'Retrasado')
    ]
    estado = models.CharField(max_length=20, choices= ESTADOS, default='activo')

    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    #FK a modelo avion (lo agregamos dsp en la app 'aviones').
    avion = models.ForeignKey('aviones.Avion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha_salida.date()})"