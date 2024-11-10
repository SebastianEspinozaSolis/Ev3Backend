from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['contenido', 'calificacion']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu reseña...'}),
            'calificacion': forms.Select()
        }
