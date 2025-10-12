from .views import catListView, catCreateView , catDeleteView, catUpdateView
from django.urls import path, include


urlpatterns = [

    path('',catListView.as_view(), name='categoria_lista'),

    path('nuevo/', catCreateView.as_view(), name='categoria_crear'),

    path('<int:pk>/editar/' , catUpdateView.as_view(), name='categoria_editar'),

    path('<int:pk>/eliminar/' ,catDeleteView.as_view(), name='categoria_eliminar'),
]

