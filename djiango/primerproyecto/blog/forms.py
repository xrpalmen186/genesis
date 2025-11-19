from django import forms
from .models import Post, Autor

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=60, label="Nombre del autor: ")
    apellido = forms.CharField(max_length=60)
    edad = forms.IntegerField(max_value=120, required=False)
    email = forms.EmailField(max_length=50)
    
    
class AutorModelFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'edad', 'email'] # de esta forma nos basamos en el modelo Autor, un formulario basado en un modelo, le decimos el modelo y los campos que quiero.