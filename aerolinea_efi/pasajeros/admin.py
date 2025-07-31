from django.contrib import admin

# Register your models here.
from .models import Pasajero

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'email', 'telefono', 'nacionalidad',)
    search_fields = ('nombre', 'apellido', 'documento', 'email',)
    list_filter = ('nacionalidad',)