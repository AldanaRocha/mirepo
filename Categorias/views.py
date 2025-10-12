from django.shortcuts import render
from .models import Categoria
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, View, UpdateView
from django.urls import reverse_lazy



class catListView(ListView):
  model=Categoria
  template_name = 'categoria_lista.html'

class catCreateView(CreateView):
  model=Categoria
  template_name='categoria_crear.html'
  fields=['nombre','descripcion']

  def get_success_url(self):
    return reverse_lazy('categoria_lista')
  

class catDeleteView(DeleteView):
    model=Categoria
    success_url=reverse_lazy('categoria_lista')

class catUpdateView(UpdateView):
   model=Categoria
   template_name= 'categoria_editar.html'
   fields=['nombre','descripcion']
   success_url= reverse_lazy('categoria_lista')