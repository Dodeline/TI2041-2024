from django.urls import path
from .views import lista_productos, detalle_producto, agregar_producto

urlpatterns = [
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/<int:id>/', detalle_producto, name='detalle_producto'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
]
