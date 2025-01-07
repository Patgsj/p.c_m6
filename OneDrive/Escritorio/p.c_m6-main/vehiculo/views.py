from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo
from .forms import VehiculoForm

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listado_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('precio')
    vehiculos_bajo = []
    vehiculos_medio = []
    vehiculos_alto = []

    for vehiculo in vehiculos:
        if vehiculo.precio is not None:
            if vehiculo.precio <= 10000:
                vehiculos_bajo.append(vehiculo)
            elif 10000 < vehiculo.precio <= 30000:
                vehiculos_medio.append(vehiculo)
            else:
                vehiculos_alto.append(vehiculo)

    context = {
        'vehiculos_bajo': vehiculos_bajo,
        'vehiculos_medio': vehiculos_medio,
        'vehiculos_alto': vehiculos_alto,
    }
    return render(request, 'vehiculo/vehiculo_listado.html', context)

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:listado')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/vehiculo_form.html', {'form': form})

@login_required
@permission_required('vehiculo.delete_vehiculo', raise_exception=True)
def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo:listado')
    return render(request, 'vehiculo/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})

@login_required
def index(request):
    return render(request, 'vehiculo/index.html')
