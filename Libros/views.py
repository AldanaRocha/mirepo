from .models import Libro
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class LibrosListView(ListView):
    model=Libro
    template_name='lista_libros.html'
    libros='libros'

    #paginator = Paginator(libros, 5) 



class LibrosCreateView(CreateView):
    model=Libro
    template_name='libros_crear.html'
    fields=['titulo','autor','año','disponible','categoria']

    def get_success_url(self):
     return reverse_lazy('lista_libros')
  
class LibroUpdateView(UpdateView):
   model = Libro
   template_name = 'libros_editar.html'
   fields=['titulo','autor','año','disponible','categoria']
   success_url= reverse_lazy('lista_libros')


class LibroDeleteView(DeleteView):
   model = Libro
   success_url = reverse_lazy('lista_libros')
   