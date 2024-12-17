from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate
from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError
from .models import Producto  # Asegúrate de que el modelo Producto esté creado en productos/models.py
from .utils import generar_token, JWTAuth  # Necesitas tener esta función en utils.py

# Crea la API
api = NinjaAPI(
    title="API de Productos",
    description="API para gestionar productos en la tienda",
    version="1.0.0"
)

# Crea el objeto auth para autenticación JWT
auth = JWTAuth()

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
                               {'response': 'Recurso no encontrado'},
                               status=404)

@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
                               {
                                   'response': 'Error de Formato de Entrada',
                                   'errores': ex.errors()
                               },
                               status=422)

# Modelo para solicitud de token de autenticación
class AuthRequest(Schema):
    username: str
    password: str

# Servicio para obtener el token de autenticación
@api.post(path="/token", tags=["Auth"])
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return { "error": "Credenciales inválidas" }
    token = generar_token(user)  # Genera el token con la función generar_token
    return { "token": token }

# Servicio para obtener todos los productos
@api.get(path="productos/", auth=auth, tags=["Productos"])
def get_productos(request):
    productos = Producto.objects.all().order_by('nombre').values()  # Puedes ordenarlos como prefieras
    return list(productos)

# Servicio para obtener un producto específico por ID
@api.get(path="productos/{producto_id}", tags=["Productos"])
def get_producto(request, producto_id: int):
    producto = get_object_or_404(Producto, id=producto_id)
    return {"id": producto.id, "nombre": producto.nombre, "precio": producto.precio, "descripcion": producto.descripcion}

# Esquema para crear y actualizar productos
class ProductoSchema(Schema):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria_id: int  # O cualquier otro campo que desees agregar

# Servicio para agregar un nuevo producto
@api.post(path="productos/", auth=auth, tags=["Productos"])
def add_producto(request, data: ProductoSchema):
    producto = Producto.objects.create(**data.dict())
    return { "id": producto.id, "nombre": producto.nombre }

# Servicio para actualizar un producto existente
@api.put(path="productos/{producto_id}", auth=auth, tags=["Productos"])
def update_producto(request, producto_id: int, data: ProductoSchema):
    producto = get_object_or_404(Producto, id=producto_id)
    for attr, value in data.dict().items():
        setattr(producto, attr, value)
    producto.save()
    return { "id": producto.id, "nombre": producto.nombre }

# Servicio para eliminar un producto
@api.delete(path="productos/{producto_id}", auth=auth, tags=["Productos"])
def delete_producto(request, producto_id: int):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return {"message": "Producto eliminado con éxito"}
    return {"message": "Post eliminado con éxito"}
