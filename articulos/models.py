from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    costo = models.IntegerField()
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo