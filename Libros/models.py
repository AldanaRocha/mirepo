from django.db import models
from Categorias.models import Categoria
from django.urls import reverse

class Libro(models.Model):
    titulo=models.CharField()
    autor=models.CharField()
    año=models.IntegerField()
    disponible=models.BooleanField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
    def get_absolute_url(self):
        return reverse('lista_libros', kwargs={'pk': self.pk})    