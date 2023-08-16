from django.shortcuts import render, redirect, render, get_object_or_404, redirect
from .forms import PacienteForm, CitaForm, DentistaForm, BuscarDentistaForm
from .models import Paciente, Cita, Dentista

def home(request):
    return render(request, "aplicacion/home.html" )

def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes') 
    else:
        form = PacienteForm()
    return render(request, 'aplicacion/agregar_paciente.html', {'form': form})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'aplicacion/lista_pacientes.html', {'pacientes': pacientes})

def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'aplicacion/agendar_cita.html', {'form': form})

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'aplicacion/lista_citas.html', {'citas': citas})

def agregar_dentista(request):
    if request.method == 'POST':
        form = DentistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_dentistas') 
    else:
        form = DentistaForm()
    return render(request, 'aplicacion/agregar_dentista.html', {'form': form})

def lista_dentistas(request):
    dentistas = Dentista.objects.all()
    return render(request, 'aplicacion/lista_dentistas.html', {'dentistas': dentistas})

def buscar_profesionales(request):
    form = BuscarDentistaForm(request.GET)
    dentistas = []

    if form.is_valid():
        especialidad = form.cleaned_data['especialidad']
        dentistas = Dentista.objects.filter(especialidad__icontains=especialidad)

    return render(request, 'aplicacion/buscar_profesionales.html', {'form': form, 'dentistas': dentistas})


