from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirmacion = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    # Campos para el perfil
    nombre = forms.CharField(max_length=100, required=True, label='Nombre')
    rol = forms.ChoiceField(choices=Perfil.ROLES, label='Rol')
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmacion']  # Campos del modelo User

    def clean_password_confirmacion(self):
        password = self.cleaned_data.get('password')
        password_confirmacion = self.cleaned_data.get('password_confirmacion')
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirmacion
