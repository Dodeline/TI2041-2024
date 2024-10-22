from django import forms
from .models import Producto, Marca, Categoria, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'categoria', 'precio', 'stock', 'descripcion', 'caracteristicas']
        widgets = {
            'caracteristicas': forms.CheckboxSelectMultiple(),
        }
