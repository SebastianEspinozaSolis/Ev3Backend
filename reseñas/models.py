from django.db import models
from django.contrib.auth.models import User
from articulos.models import Publicacion

class Reseña(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='reseñas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='reseñas', on_delete=models.CASCADE)
    contenido = models.TextField()
    calificacion = models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])
    fecha_resena = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.usuario.username} para {self.publicacion.titulo}'
