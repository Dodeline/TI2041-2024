from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Producto, Caracteristica, Categoria, Marca
from .forms import ProductoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/')
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

def login_view(request):
    if request.method == 'POST':
        user = request.POST["username"]
        pswd = request.POST["password"]
        usuario = authenticate(request, username=user, password=pswd)
        if user is None:
            return HttpResponse("error de autenticación", status=401)
        
        login(request, user=usuario)
        return redirect('productos/')  # Cambia 'index' por la vista que quieras redirigir
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')