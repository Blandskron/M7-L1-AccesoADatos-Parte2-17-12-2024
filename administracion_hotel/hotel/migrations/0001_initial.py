# Generated by Django 5.1.4 on 2024-12-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_salida', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_habitacion', models.CharField(max_length=10, unique=True)),
                ('tipo_habitacion', models.CharField(choices=[('SIMPLE', 'Simple'), ('GRANDE', 'Grande'), ('SUITE', 'Suite')], max_length=10)),
                ('precio_por_noche', models.DecimalField(decimal_places=2, max_digits=6)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
