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
    origen = models.ForeignKey(Aeropuerto, related_name='vuelos_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Aeropuerto, related_name='vuelos_destino', on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField()
    fehca_llegada = models.DateTimeField()
    duracion = models.DurationField(null= True, blank= True)
    tripulacion = models.ManyToManyField(Tripulante, blank=True)

    ESTADOS = [
        ('activo', 'Activo'),
        ('cancelado', 'Cancelado'),
        ('retrasado', 'Retrasado')
    ]
    estado = models.CharField(max_length=20, choices= ESTADOS, default='activo')

    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    avion = models.ForeignKey('aviones.Avion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha_salida.date()})"


class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    asiento = models.CharField(max_length=5) #ej: "12A"
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    precio_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    clase = models.ForeignKey(Asiento, on_delete=models.SET_NULL, null=True, blank=True)

    ESTADOS_RESERVA = [
        ('confirmada', 'Confirmada')
        ('cancelada', 'Cancelada')
        ('pendiente', 'Pendiente')
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA, default='pendiente')

    def __str__(self):
        return f"Reserva {self.id} - {self.pasajero} - {self.vuelo}"


class Aeropuerto(models.Model):
    codigo_iata = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo_iata} - {self.nombre}"


class Tripulante(models.Model): 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100) #piloto, copiloto, auxiliar, pasajero, etc.

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"


class Asiento(models.Model):
    nombre = models.CharField(max_length=50) #economica, business, primera.
    precio_adicional = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre
