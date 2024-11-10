from django.urls import path
from . import views

app_name = 'articulos'

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('editar/<int:pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('mis-articulos/', views.mis_articulos, name='mis_articulos'),
]