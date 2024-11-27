from django.contrib import admin
from .models import Perfil
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    list_display=["rol","nombre"]

admin.site.register(Perfil,PerfilAdmin)