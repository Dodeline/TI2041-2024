from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True)
    caracteristicas = models.ManyToManyField(Caracteristica, blank=True)

    def __str__(self):
        return self.nombre

