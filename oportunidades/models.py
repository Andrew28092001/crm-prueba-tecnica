from django.db import models
from clientes.models import Cliente

class Oportunidad(models.Model):
    ESTADOS = [
        ('Nuevo', 'Nuevo'),
        ('Contactado', 'Contactado'),
        ('En negociación', 'En negociación'),
        ('En seguimiento', 'En seguimiento'), # Añadido para la automatización 
        ('Cerrado', 'Cerrado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='oportunidades') # FK requerida 
    descripcion = models.TextField()
    valor_estimado = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Nuevo')
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Fecha automática 

    def __str__(self):
        return f"{self.descripcion} - {self.cliente.nombre_completo}"