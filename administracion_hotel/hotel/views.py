from django.shortcuts import render
from django.db import connection
from .models import Cliente, Habitacion

# Consultas directa a Base de Datos 
def habitacion_disponible_base_datos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hotel_habitacion WHERE disponible = TRUE")
        rows = cursor.fetchall()

    return render(request, 'habitaciones_db.html', {'habitaciones': rows})

def lista_clientes_base_datos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hotel_cliente ORDER BY fecha_ingreso DESC")
        rows = cursor.fetchall()

    return render(request, 'clientes_db.html', {'clientes': rows})

# Consultas indirecta mediante el modelo a la Base de Datos 
def habitacion_disponible(request):
    habitaciones = Habitacion.objects.raw('SELECT * FROM hotel_habitacion WHERE disponible = TRUE')
    return render(request, 'habitaciones.html', {'habitaciones': habitaciones})

def lista_clientes(request):
    clientes = Cliente.objects.raw('SELECT * FROM hotel_cliente ORDER BY fecha_ingreso DESC')
    return render(request, 'clientes.html', {'clientes': clientes})