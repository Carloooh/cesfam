from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('medico', views.medico),
    path('farmacia', views.farmacia)
]
