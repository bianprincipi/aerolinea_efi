from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Empleado', 'Empleado'),
        ('Cliente', 'Cliente')
    ]

    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} ({self.rol})"