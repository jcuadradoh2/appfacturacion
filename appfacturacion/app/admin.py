from django.contrib import admin
from .models import Producto, Cliente, Factura, DetalleFactura
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['iva']
    list_display = ('descripcion','precio')
    ordering = ('descripcion',)
    search_fields = ('descripcion', 'precio', 'stock')
    list_filter = ('descripcion',)


admin.site.register(Producto, ProductoAdmin)