from django.shortcuts import render

# Create your views here.
productos = []

# Lista los productos
def lista_productos(request):
    return render(request, 'consulta.html', {'productos': productos})

# Crea un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        nuevo_producto = {'nombre': nombre, 'precio': precio}
        productos.append(nuevo_producto)  # Se almacena el producto en memoria
        return render(request, 'resultado.html', {'producto': nuevo_producto})
    return render(request, 'registro.html')

# Resultado de validación
def resultado_producto(request):
    return render(request, 'resultado.html')