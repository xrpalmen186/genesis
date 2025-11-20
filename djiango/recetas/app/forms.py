from django import forms
from .models import *

class FiltroIngredientesForm(forms.ModelForm):
    ingrediente = forms.CharField(label='Ingrediente', max_length=100)
    
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria']