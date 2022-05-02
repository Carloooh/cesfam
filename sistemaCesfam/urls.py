from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.index),
    path('main/', views.main),
    # path('farmaceutico', views.farmaceutico),
    # path('medico', views.medico),
]
