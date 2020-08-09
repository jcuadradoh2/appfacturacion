from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from .forms import *
from .models import *
from datetime import datetime
from django.db.models import Sum
from django.db.models.functions import Coalesce


# Create your views here.
def menu(request):
    data=[]    
    year=datetime.now().year
    for m in range(1,13):
        total=DetalleFactura.objects.filter(creacion__year=year, creacion__month=m).aggregate(r=Coalesce(Sum('subtotal'),0)).get('r')
        #total = DetalleFactura.objects.select_related('producto').filter(creacion__year=year, creacion__month=m).values('producto__descripcion').annotate(total=Sum('subtotal')).order_by('subtotal')
        data.append(float(total))            
        #data[total[0]]=total[1]
    opciones = {'Menu': 'Dashboard','Nombre':'Modulo de Facturacion','data_chart': data, 'year':year}
    return render(request, 'dashboard.html', opciones)

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('index')

def cliente(request):
    c=Cliente.objects.select_related('producto').values('id', 'ruc', 'nombre', 'direccion', 'producto__descripcion')
    opciones = {'Menu': 'Clientes','accion': 'Nuevo', 'clientes':c}    
    return render(request, 'cliente-view.html', opciones)   


def cliente_save(request):
    opciones = {'Titulo': 'Agregar cliente', 'accion': 'Guardar'}
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
    

