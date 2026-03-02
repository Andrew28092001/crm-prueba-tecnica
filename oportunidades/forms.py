from django import forms
from .models import Oportunidad

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ['cliente', 'descripcion', 'valor_estimado', 'estado']
        widgets = {
            # forms.Select crea una lista desplegable automática con los clientes que existan
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor_estimado': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }