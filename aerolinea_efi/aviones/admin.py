from django.contrib import admin

# Register your models here.

from .models import Avion

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'capacidad', 'filas', 'columnas') #muestra esas columnas en la tabla del admin.
    search_fields = ('modelo',) #agrega una barra de busqueda por el campo modelo.
    list_filter = ('capacidad',) #agrega un filtro por capacidad.