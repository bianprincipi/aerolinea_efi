from django.db import models
from django.shortcuts import render
from vuelos.models import Vuelo
from reservas.models import Reserva

# Create your models here.

def reporte_pasajeros_por_vuelo(request):
    vuelos = Vuelo.objects.all()
    reservas = None
    vuelo_seleccionado = None

    if request.method == 'POST':
        vuelo_id = request.POST.get('vuelo')
        vuelo_seleccionado = Vuelo.objects.get(id=vuelo_id)
        reservas = Reserva.objects.filter(vuelo=vuelo_seleccionado)

        return render(request, 'reportes/pasajeros_por_vuelo.html', {
            'vuelos': vuelos,
            'reservas': reservas,
            'vuelo_seleccionado': vuelo_seleccionado
        })
