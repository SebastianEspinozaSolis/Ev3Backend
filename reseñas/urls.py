from django.urls import path
from . import views

app_name = 'reseñas'

urlpatterns = [
    path('crear/<int:pk>/', views.crear_reseña, name='crear_reseña'),
    path('mis-reseñas/', views.mis_reseñas, name='mis_reseñas'),
    path('editar/<int:pk>/', views.editar_reseña, name='editar_reseña'),
]