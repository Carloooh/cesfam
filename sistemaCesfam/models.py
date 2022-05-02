from django.db import models

# Create your models here.

class Medicamento(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    stock = models.IntegerField()
    estado = models.CharField(max_length=50)

class Usuario(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    rut = models.IntegerField()
    digitoVer = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    contra = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=50)

class Paciente(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    rut = models.IntegerField()
    digitoVer = models.CharField(max_length=1)
    nombre = nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    celular = models.IntegerField()

class Meds_Entregados(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    receta_id = models.CharField(max_length=9)

class Receta(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    fecha = models.CharField(max_length=500)