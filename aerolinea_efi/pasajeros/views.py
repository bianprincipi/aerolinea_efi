from django.shortcuts import render, redirect
from .models import Pasajero
from django import forms


class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = ['nombre', 'apellido', 'documento', 'email', 'telefono', 'fecha_nacimiento']


def lista_pasajeros(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'pasajeros/lista_pasajeros.html', {'pasajeros': pasajeros})


def crear_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pasajeros')
    else:
        form = PasajeroForm()
    return render(request, 'pasajeros/crear_pasajero.html', {'form': form})
