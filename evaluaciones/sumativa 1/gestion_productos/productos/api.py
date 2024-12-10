from ninja import NinjaAPI

api = NinjaAPI()

from .models import Categoria

@api.get("/categories")
def get_categories(request):
    categories = Categoria.objects.values("id", "nombre", "descripcion")
    return {"categories": list(categories)}

from .models import Marca

@api.get("/brands")
def get_brands(request):
    brands = Marca.objects.values("id", "nombre", "descripcion")
    return {"brands": list(brands)}
from .models import Producto

@api.get("/products")
def get_products(request, brand_id: int = None, category_id: int = None):
    products = Producto.objects.all()

    if brand_id:
        products = products.filter(marca_id=brand_id)
    if category_id:
        products = products.filter(categoria_id=category_id)

    products = products.values("id", "nombre", "precio", "marca__nombre", "categoria__nombre")
    return {"products": list(products)}
