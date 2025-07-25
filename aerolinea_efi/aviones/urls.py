from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aviones, name='lista_aviones'),
    path('crear/', views.crear_avion, name='crear_avion'),
]
