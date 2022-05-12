from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'main.html')

def farmacia(request):
    return render(request,'farmacia.html')

def medico(request):
    return render(request,'medico.html')

def contacto(request):
    
    if request.method=="POST":
        
        
        
        return render(request, "confirmacion.html")
    
    return render(request, 'solicitud.html')