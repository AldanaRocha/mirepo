from django.db import models

class Categoria(models.Model):
    nombre=models.CharField(unique=True)
    descripcion=models.TextField(blank=True, null=True)

    def __str__(self):
     return f'nombre: {self.nombre} - descripcion: {self.descripcion}'
    
