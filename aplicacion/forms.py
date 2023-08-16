from django import forms
from .models import Cita, Paciente, Dentista


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email']


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['dia', 'mes', 'anio', 'descripcion']


class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentista 
        fields = ['nombre', 'especialidad']


class BuscarDentistaForm(forms.Form):
    especialidad = forms.CharField(max_length=100, label='Especialidad')
    