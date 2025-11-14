# shop/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if not p1 or not p2:
            raise forms.ValidationError("Debes escribir la contraseña dos veces.")
        if p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# Usamos el PasswordChangeForm de Django (puede usarse directamente en la vista)
# Si quieres un formulario simple para cambiar contraseña sin pedir la antigua,
# te recomiendo usar el form oficial para seguridad.

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('balance',)  # si solo quieres permitir ver/editar el balance desde admin, puedes quitarlo aquí

class AddBalanceForm(forms.Form):
    amount = forms.DecimalField(label='Cantidad a añadir (€)', max_digits=8, decimal_places=2, min_value=0.01)
