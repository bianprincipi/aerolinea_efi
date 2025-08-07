from django.db import models

class Pasajero(models.Model):
    TIPO_DOCUMENTO = [
        ('DNI', 'DNI'),
        ('Pasaporte', 'Pasaporte'),
        ('Otro', 'Otro')
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True)
    tipo_documento = models.CharField(max_length=20, choices=TIPO_DOCUMENTO)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre