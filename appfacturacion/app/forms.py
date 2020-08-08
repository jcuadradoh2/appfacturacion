from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion', 'producto')

        label = {'ruc': 'Ruc', 'nombre': 'Nombre','direccion': 'Direccion'}
