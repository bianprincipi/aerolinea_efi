from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pasajeros, name='lista_pasajeros'),
    path('crear/', views.crear_pasajero, name='crear_pasajero'),
]
