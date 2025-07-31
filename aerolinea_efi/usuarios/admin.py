from django.contrib import admin

# Register your models here.
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'cargo', 'activo', 'fecha_ingreso', 'es_administrador', 'es_personal_vuelo',)
    list_filter = ('activo', 'es_administrador', 'es_personal_vuelo', 'cargo',)
    search_fields = ('nombre', 'apellido', 'documento', 'cargo',)
    ordering = ('apellido', 'nombre',)