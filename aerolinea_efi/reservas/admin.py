from django.contrib import admin

# Register your models here.
from .models import Reserva, Boleto

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('vuelo', 'pasajero', 'asiento', 'fecha_reserva',)
    list_filter = ('vuelo', 'fecha_reserva',)
    ordering = ('-fecha_reserva',)

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'reserva', 'emitido',)
    ordering = ('-emitido',)