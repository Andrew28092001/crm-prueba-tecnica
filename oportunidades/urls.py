from django.urls import path
from . import views

urlpatterns = [
    path('', views.OportunidadListView.as_view(), name='oportunidad_list'),
    path('nueva/', views.OportunidadCreateView.as_view(), name='oportunidad_create'),
    path('<int:pk>/editar/', views.OportunidadUpdateView.as_view(), name='oportunidad_update'),
    path('<int:pk>/eliminar/', views.OportunidadDeleteView.as_view(), name='oportunidad_delete'),
]