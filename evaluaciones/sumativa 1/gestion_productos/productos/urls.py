from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', views.lista_productos ),
    path('', api.urls view lista de productos),   # Ruta para la API de productos
]

