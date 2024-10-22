from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Caracteristica, Categoria, Marca
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    # Obtener todas las marcas, categorías y características
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    caracteristicas = Caracteristica.objects.all()
    
    return render(request, 'productos/agregar_producto.html', {
        'form': form,
        'marcas': marcas,
        'categorias': categorias,
        'caracteristicas': caracteristicas,
    })
