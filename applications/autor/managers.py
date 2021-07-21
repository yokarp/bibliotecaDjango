from django.db import models

class AutorManager(models.Manager):
    """ Manager para el modelo autor"""

    def listar_autores(self):
        return self.all()