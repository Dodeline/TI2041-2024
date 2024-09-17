from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # Lista de productos
    path('crear/', views.crear_producto, name='crear_producto'),  # Registro de productos
    path('resultado/', views.resultado_producto, name='resultado_producto'),  # Resultado de validación
]