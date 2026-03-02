from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=150)
    empresa = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True) # Fecha automática 

    def __str__(self):
        return self.nombre_completo