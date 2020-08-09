"""appfacturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='index'),
    #path('cliente/', cliente, name='cliente'),
    path('logout/', logout, name='logout'), 
    path('cliente_save/', cliente_save, name='guardarcliente'), 
    path('cliente_view/', cliente, name='listarcliente'), 
    path('cliente_delete/<int:id>', cliente_delete, name='eliminarcliente'),
    path('cliente_edit/<int:id>', cliente_edit, name='editarcliente'),
    path('producto/', producto, name='producto'),
    path('listarproducto/', listarProducto, name='listarproducto'),
    path('editarproducto/<int:id>/', editarProducto, name='editarproducto'),
    path('eliminarproducto/<int:id>', eliminarProducto, name='eliminarproducto'),
    path('producto_save/', producto_save, name='guardarproducto'), 
    path('ventas/', ventas, name='ventas'), 
]
