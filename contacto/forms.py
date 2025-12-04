from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@email.com'}),
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Escribe tu mensaje para cotización...'}),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
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
            Field('message', css_class='form-group mb-4'),
            Submit('submit', 'Enviar mensaje', css_class='btn btn-primary btn-lg w-100')
        )
