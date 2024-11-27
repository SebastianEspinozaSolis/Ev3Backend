from django.urls import path
from . import views

app_name = 'reseñas'

urlpatterns = [
    path('crear/<int:pk>/', views.crear_reseña, name='crear_reseña'),
    path('mis-reseñas/', views.mis_reseñas, name='mis_reseñas'),
    path('editar/<int:pk>/', views.editar_reseña, name='editar_reseña'),
    path('api/',views.reseñas_api,name='api_reseñas'),
    path('api_detalle/<int:pk>/',views.reseñas_api_detalle,name='api_reseñas'),
]