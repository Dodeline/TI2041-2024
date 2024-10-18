# sumativa-1
prueba 1 Back End
- **models.py**: Contiene los modelos de datos para Marca, Categoria, Caracteristica y Producto.
- **views.py**: Define las vistas, incluyendo la lista de productos.
- **urls.py**: Configura las rutas para acceder a las vistas.
- **templates/**: Contiene las plantillas HTML, incluyendo lista_productos.html.

## Requisitos Previos

- Python 3.x
- Django 3.x o superior
- SQLite3 (incluido con Django)

## Instrucciones para Ejecutar

1. Clonar el repositorio.
2. Crear un entorno virtual y activarlo.
3. Instalar las dependencias con `pip install -r requirements.txt`.
4. Realizar las migraciones con `python manage.py migrate`.
5. Crear un superusuario con `python manage.py createsuperuser` y acceder al admin.
6. Correr el servidor con `python manage.py runserver`.
7. Visitar `http://127.0.0.1:8000/productos/` para ver la lista de productos.
5. Verificar Errores