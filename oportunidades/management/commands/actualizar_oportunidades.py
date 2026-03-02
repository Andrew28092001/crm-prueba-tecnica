from django.core.management.base import BaseCommand
from oportunidades.models import Oportunidad
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = "Marca como 'En seguimiento' las oportunidades con más de 7 días en estado 'Nuevo'."

    def handle(self, *args, **kwargs):
        hace_7_dias = timezone.now() - timedelta(days=7)
        
        # Filtramos oportunidades 'Nuevo' creadas hace más de 7 días
        oportunidades = Oportunidad.objects.filter(
            estado='Nuevo',
            fecha_creacion__lt=hace_7_dias
        )
        
        cantidad = oportunidades.update(estado='En seguimiento')
        
        self.stdout.write(self.style.SUCCESS(f'Éxito: Se actualizaron {cantidad} oportunidades a "En seguimiento".'))