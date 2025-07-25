from django.shortcuts import render, redirect
from .models import Avion
from django import forms


class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas']


def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'aviones/lista_aviones.html', {'aviones': aviones})


def crear_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aviones')
    else:
        form = AvionForm()
    return render(request, 'aviones/crear_avion.html', {'form': form})
