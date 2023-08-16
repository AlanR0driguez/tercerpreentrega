from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('Buscar Profesionales/', buscar_profesionales, name='buscar_profesionales'),
    path('Registrar paciente/', agregar_paciente, name='agregar_paciente'),
    path('Lista de pacientes/', lista_pacientes, name='lista_pacientes'),
    path('Agendar cita/', agendar_cita, name='agendar_cita'),
    path('Lista de citas/', lista_citas, name='lista_citas'),
    path('Nuestros Dentistas/', lista_dentistas, name='lista_dentistas'),
    path('Agregar Dentista/', agregar_dentista, name='agregar_dentista'),
]