from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field
from .models import Mural
from contacto.models import MuralQuote


class MuralSubmissionForm(forms.ModelForm):
    # Campo para la ubicación (se guardará directamente en el modelo Mural)
    location = forms.CharField(
        max_length=200,
        required=False,
        label='Ubicación',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ubicación del mural'
        }),
        help_text='Indica la ubicación del mural (opcional).'
    )

    class Meta:
        model = Mural
        fields = ('title', 'description', 'image', 'location', 'technique', 'dimensions', 'year')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del mural'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Descripción del mural'
            }),
            'technique': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Técnica utilizada'
            }),
            'dimensions': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dimensiones (ej: 5m x 3m)'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Año'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'image': 'Imagen',
            'technique': 'Técnica',
            'dimensions': 'Dimensiones',
            'year': 'Año',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        # location ya está en cleaned_data/model field porque lo incluimos en Meta.fields
        if commit:
            instance.save()
        return instance


class MuralQuoteForm(forms.ModelForm):
    class Meta:
        model = MuralQuote
        fields = ('name', 'email', 'technique', 'dimensions', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@email.com', 'class': 'form-control'}),
            'technique': forms.TextInput(attrs={'placeholder': 'Ej: Pintura acrílica, aerosol, etc.', 'class': 'form-control'}),
            'dimensions': forms.TextInput(attrs={'placeholder': 'Ej: 3m x 2m, 5m x 4m, etc.', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Describe tu proyecto o cualquier detalle adicional', 'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'technique': 'Técnica',
            'dimensions': 'Dimensiones',
            'message': 'Mensaje',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('technique', css_class='form-group col-md-6 mb-3'),
                Column('dimensions', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('message', css_class='form-group mb-4'),
            Submit('submit', 'Enviar Cotización', css_class='btn btn-primary btn-lg w-100')
        )

