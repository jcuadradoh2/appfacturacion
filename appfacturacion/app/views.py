from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from .forms import *
from .models import *
from datetime import datetime
# Create your views here.
def menu(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blogs', 'Nombre':'Modulo de Facturacion'}

    return render(request, 'menu.html', opciones)

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


def cliente(request):
    c=Cliente.objects.select_related('producto').values('id', 'ruc', 'nombre', 'direccion', 'producto__descripcion')

    opciones = {'Menu': 'Clientes',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Nuevo', 'clientes':c}    
    return render(request, 'cliente-view.html', opciones)   


def cliente_save(request):
    opciones = {'Menu': 'Agregar Clientes', 'accion': 'Guardar'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            c = Cliente.objects.first()
            p = Producto.objects.first()
            hoy = datetime.now()
            Factura.objects.create(cliente = c, fecha = hoy, total = p.precio)
            f = Factura.objects.first()
            DetalleFactura.objects.create(factura = f, producto = p, cantidad = 1, precio = p.precio, subtotal = 4)
            
            return redirect('listarcliente')
    else:
        form = ClienteForm()
        opciones['form'] = form        
    return render(request, 'cliente-edit.html', opciones)


def cliente_edit(request, id):
    opciones = {'Titulo': 'Editar cliente','accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    return render(request, 'cliente-edit.html', opciones)


def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        cliente.delete()                
    return redirect('listarcliente')

    ######################################################################

def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    return render(request, 'listar_producto.html', opciones )
    

def producto_save(request):
    opciones = {'Menu': 'Agregar Productos', 'accion': 'Guardar'}
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form
    return render(request, 'editarProducto.html', opciones)


def editarProducto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')

    return render(request, 'editarProducto.html', opciones)


def listarProducto(request):
    producto = Producto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto del Blog', 'Acerca': 'Acerca del Blog', 'productos': producto}
    return render(request, 'listar_producto.html', opciones)


def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        producto.delete()
        return redirect('listarproducto')
    #return render(request, 'eliminar_producto.html', {'Contacto': producto})


        ######################################################################

def ventas(request):
    ventas = DetalleFactura.objects.select_related('factura','producto').values('id','factura__cliente__nombre', 'producto__descripcion', 'factura__total')
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto del Blog', 'Acerca': 'Acerca del Blog', 'ventas': ventas}
    return render(request, 'ventas.html', opciones)