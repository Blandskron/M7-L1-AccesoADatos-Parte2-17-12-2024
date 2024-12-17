from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
class Habitacion(models.Model):
    TIPO_HABITACION = [
        ('SIMPLE', 'Simple'),
        ('GRANDE', 'Grande'),
        ('SUITE', 'Suite'),
    ]

    numero_habitacion = models.CharField(max_length=10, unique=True)
    tipo_habitacion = models.CharField(max_length=10, choices=TIPO_HABITACION)
    precio_por_noche = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Habitacion {self.numero_habitacion} ({self.get_tipo_habitacion_display()})"