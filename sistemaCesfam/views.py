from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    return render(request,'login.html')

def cerrarSesion(request):
    logout(request)
    return redirect(request,'login.html')

@login_required
def main(request):
    return render(request, 'main.html')
# def farmaceutico(request):
#     return render(request,'farmaceutico.html')

# def medico(request):
#     return render(request,'medico.html')
