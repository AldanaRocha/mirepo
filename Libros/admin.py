from django.contrib import admin
from .models import Libro


admin.site.register(Libro)

class LibroAdmin(admin.ModelAdmin):
    lista= ['titulo', 'autor', 'año', 'disponible']