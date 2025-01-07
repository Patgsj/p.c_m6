from django.urls import path
from . import views

app_name = 'vehiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.listado_vehiculos, name='listado'),
    path('add/', views.agregar_vehiculo, name='add'),
    path('<int:pk>/delete/', views.eliminar_vehiculo, name='eliminar'),
]
