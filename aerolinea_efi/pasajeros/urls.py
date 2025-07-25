from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pasajeros, name='lista_pasajeros'),
    path('nuevo/', views.crear_pasajero, name='crear_pasajero'),
]
