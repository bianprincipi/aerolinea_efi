from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField()
    columnas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.modelo} ({self.capacidad} asientos)"

class Asiento(models.Model):
    TIPOS = [
        ('Economico', 'Economico'),
        ('Ejecutivo', 'Ejecutivo')
    ]
    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Reservado', 'Reservado'),
        ('Ocupado', 'Ocupado')
    ]

    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    numero = models.CharField(max_length=5)
    fila = models.PositiveIntegerField()
    columna = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Disponible')

    def __str__(self):
        return f"Asiento {self.numero} - {self.avion.modelo}"