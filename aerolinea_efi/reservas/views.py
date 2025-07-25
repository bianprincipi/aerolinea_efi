from django.http import HttpResponse

def lista_pasajeros(request):
    return HttpResponse("Lista de pasajeros")

def crear_pasajero(request):
    return HttpResponse("Crear pasajero")
