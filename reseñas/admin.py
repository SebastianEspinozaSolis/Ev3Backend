from django.contrib import admin
from .models import Reseña
# Register your models here.
class ReseñaAdmin(admin.ModelAdmin):
    list_display=["contenido","calificacion"]
admin.site.register(Reseña,ReseñaAdmin)