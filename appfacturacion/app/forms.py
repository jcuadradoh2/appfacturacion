from django import forms
from .models import Cliente, Producto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion', 'producto')

        label = {'ruc': 'Ruc', 'nombre': 'Nombre','direccion': 'Direccion'}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock')
        label = {'Descripcion':'descripcion', 'precio':'Precio', 'stock':'Stock'}