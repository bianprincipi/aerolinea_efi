from django.contrib import admin

# Register your models here.
from .models import Aeropuerto, Tripulante, AsientoClase, Vuelo

@admin.register(Aeropuerto)
class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ('codigo_iata', 'nombre', 'ciudad', 'pais',)
    search_fields = ('codigo_iata', 'nombre', 'ciudad', 'pais',)
    ordering = ('codigo_iata',)

@admin.register(Tripulante)
class TripulanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo',)
    search_fields = ('nombre', 'apellido', 'cargo',)
    ordering = ('apellido', 'nombre')

@admin.register(AsientoClase)
class AsientoClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_adicional',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'fecha_salida', 'fecha_llegada', 'estado', 'precio_base',)
    list_filter = ('estado', 'origen', 'destino', 'fecha_salida',)
    search_fields = ('origen__codigo_iata', 'destino__codigo_iata', 'avion__matricula',)  # suponiendo avion tiene matricula
    ordering = ('-fecha_salida',)
    filter_horizontal = ('tripulacion',)  # para ManyToMany con mejor interfaz
