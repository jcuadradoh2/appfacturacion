from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from .forms import *
from .models import *
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