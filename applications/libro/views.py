from django.db import models
from django.shortcuts import render

from django.views.generic import ListView

# models local
from .models import Libro

class ListLibros(ListView):
    # model = Autor
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        f1 = self.request.GET.get("fecha1", '')
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return Libro.objects.listar_libros(palabra_clave)
        else:
            return Libro.objects.listar_libros2(palabra_clave, f1, f2)


        
