from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    registration_key = forms.CharField(
        label='Clave de Registro',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingresa la clave de acceso',
            'class': 'form-control'
        }),
        help_text='Se requiere una clave especial para registrarse.',
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })

    def clean_registration_key(self):
        registration_key = self.cleaned_data.get('registration_key')
        if registration_key != 'root123':
            raise forms.ValidationError(
                'La clave de registro es incorrecta. Contacta al administrador para obtener la clave válida.'
            )
        return registration_key

    def save(self, commit=True):
        user = super().save(commit=False)
        # No guardamos el campo registration_key, solo lo usamos para validación
        if commit:
            user.save()
        return user

