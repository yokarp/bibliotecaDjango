from django.db import models
from django.shortcuts import render

from django.views.generic import ListView

# models local
from .models import Autor

class ListAutores(ListView):
    # model = Autor
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'
    
    def get_queryset(self):
        return Autor.objects.listar_autores()
