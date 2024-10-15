from django.contrib import admin
from .models import Marca, Categoria, Caracteristica, Producto

# Registro de modelos en el panel de administración
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Caracteristica)
admin.site.register(Producto)