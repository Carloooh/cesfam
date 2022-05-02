from atexit import register
from django.contrib import admin
from .models import Receta,Paciente, Meds_Entregados, Medicamento, Usuario

# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Receta)
admin.site.register(Meds_Entregados)