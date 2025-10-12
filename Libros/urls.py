from .views import LibrosListView,LibrosCreateView, LibroUpdateView, LibroDeleteView
from django.urls import path


urlpatterns=[

    path('lib/', LibrosListView.as_view(), name='lista_libros'),

    path('categoria/<int:id>/', LibrosListView.as_view(), name='libros_porcategoria'),

    path('nuevo_lib/', LibrosCreateView.as_view(), name='libros_crear'),

    path('<int:pk>/editar/',  LibroUpdateView.as_view(), name='libros_editar'),

    path('<int:pk>/eliminar/', LibroDeleteView.as_view(), name= 'libros_eliminar'),

]