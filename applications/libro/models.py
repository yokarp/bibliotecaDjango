from django.db import models

# from local apps
from applications.autor.models import Autor

# Create your models here.
from .managers import LibroManager


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveBigIntegerField()

    objects = LibroManager()

    def __str__(self):
        return self.titulo
