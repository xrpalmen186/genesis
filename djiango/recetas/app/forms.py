from django import forms
from .models import Ingrediente, CategoriaIngrediente

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        # usamos solo los campos que existen en tu modelo
        fields = ['nombre', 'categoria', 'refrigerado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del ingrediente',
                'maxlength': 50,
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            # el checkbox lo dejamos sin class aquí; lo añadimos en __init__ para usar form-check-input
            'refrigerado': forms.CheckboxInput(),
        }
        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'refrigerado': '¿Refrigerado?',
        }
        help_texts = {
            'nombre': 'Máx. 50 caracteres.',
        }

    # añadir clases bootstrap según tipo de widget y personalizar el Select (empty_label)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # aplicar clases a widgets que no definimos arriba (o reforzar)
        for name, field in self.fields.items():
            widget = field.widget
            widget_type = widget.__class__.__name__.lower()
            if widget_type == 'checkboxinput':
                widget.attrs.update({'class': 'form-check-input'})
            elif widget_type == 'select':
                widget.attrs.update({'class': widget.attrs.get('class', '') + ' form-select'})
            else:
                # textinput, textarea, etc.
                widget.attrs.update({'class': widget.attrs.get('class', '') + ' form-control'})

        # Para el campo categoria: mostrar un option por defecto claro
        # (esto solo afecta al rendering; si quieres obligar a escoger, el model no permite null)
        self.fields['categoria'].empty_label = '— Selecciona categoría —'

    # ejemplo de validación adicional
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise forms.ValidationError('El nombre no puede estar vacío.')
        if len(nombre) > 50:
            raise forms.ValidationError('El nombre no puede tener más de 50 caracteres.')
        return nombre



class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'refrigerado']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del ingrediente',
                'maxlength': 50,
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            # el checkbox lo dejamos sin class aquí; lo añadimos en __init__ para usar form-check-input
            'refrigerado': forms.CheckboxInput(),
        }
        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'refrigerado': '¿Refrigerado?',
        }
        help_texts = {
            'nombre': 'Máx. 50 caracteres.',
        }

class RecetaIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'refrigerado']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del ingrediente',
                'maxlength': 50,
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            # el checkbox lo dejamos sin class aquí; lo añadimos en __init__ para usar form-check-input
            'refrigerado': forms.CheckboxInput(),
        }
        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'refrigerado': '¿Refrigerado?',
        }
        help_texts = {
            'nombre': 'Máx. 50 caracteres.',
        }