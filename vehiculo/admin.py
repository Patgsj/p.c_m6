from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'categoria', 'precio']

# Register your models here.
