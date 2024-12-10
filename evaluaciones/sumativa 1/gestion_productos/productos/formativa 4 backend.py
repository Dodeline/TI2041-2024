# urls.py
from django.urls import path
from .views import login_view, logout_view, lista_productos, detalle_producto, agregar_producto

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/<int:id>/', detalle_producto, name='detalle_producto'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('api',api.urls),
]