from django.db import models

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
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

class AsientoClase(models.Model):
    nombre = models.CharField(max_length=50)
    precio_adicional = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

class Vuelo(models.Model):
    origen = models.ForeignKey(Aeropuerto, related_name='vuelos_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Aeropuerto, related_name='vuelos_destino', on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    fecha_llegada = models.DateField()
    duracion = models.DurationField(null=True, blank=True)
    avion = models.ForeignKey('aviones.Avion', on_delete=models.CASCADE)
    tripulacion = models.ManyToManyField('vuelos.Tripulante', blank=True)

    ESTADOS = [
        ('activo', 'Activo'),
        ('cancelado', 'Cancelado'),
        ('retrasado', 'Retrasado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origen.codigo_iata} → {self.destino.codigo_iata} - {self.fecha_salida}"
