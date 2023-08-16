from django.db import models

# Create your models here.
class Dentista(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} especialista en {self.especialidad}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Cita(models.Model):
    dia = models.IntegerField(default=1)
    mes = models.IntegerField(default=1)
    anio = models.IntegerField(default=2023) 
    descripcion = models.TextField(default='Describa cual es su padecimiento')  

    def __str__(self):
        return f"Cita el {self.dia}/{self.mes}/{self.anio}"