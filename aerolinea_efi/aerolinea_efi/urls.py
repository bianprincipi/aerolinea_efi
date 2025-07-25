from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin

def home_redirect(request):
    return redirect('lista_pasajeros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pasajeros/', include('pasajeros.urls')),
    path('aviones/', include('aviones.urls')),
    path('', home_redirect),  # raíz que redirige
]
