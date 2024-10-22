from django.urls import path
from .views import lista_productos, detalle_producto, agregar_producto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('<int:id>/', detalle_producto, name='detalle_producto'),
    path('agregar/', agregar_producto, name='agregar_producto'),
]
