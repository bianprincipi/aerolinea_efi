from django.db import models

# Create your models here.

class Reserva(models.Model):
    vuelo = models.ForeignKey('vuelos.Vuelo', on_delete=models.CASCADE)
    pasajero = models.ForeignKey('pasajeros.Pasajero', on_delete=models.CASCADE)
    asiento = models.OneToOneField('vuelos.Asiento', on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_Add=True)

    def __str__(self):
        return f"Reserva de {self.pasajero} en vuelo {self.vuelo}"


class Boleto(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    emitido = models.DateTimeField(auto_now_Add=True)

    def __str__(self):
        return f"Boleto {self.codigo} - {self.reserva}"