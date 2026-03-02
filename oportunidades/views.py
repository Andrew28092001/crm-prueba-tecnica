from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Oportunidad
from .forms import OportunidadForm

class OportunidadListView(ListView):
    model = Oportunidad
    template_name = 'oportunidades/oportunidad_list.html'
    context_object_name = 'oportunidades'

class OportunidadCreateView(CreateView):
    model = Oportunidad
    form_class = OportunidadForm
    template_name = 'oportunidades/oportunidad_form.html'
    success_url = reverse_lazy('oportunidad_list')

class OportunidadUpdateView(UpdateView):
    model = Oportunidad
    form_class = OportunidadForm
    template_name = 'oportunidades/oportunidad_form.html'
    success_url = reverse_lazy('oportunidad_list')

class OportunidadDeleteView(DeleteView):
    model = Oportunidad
    template_name = 'oportunidades/oportunidad_confirm_delete.html'
    success_url = reverse_lazy('oportunidad_list')