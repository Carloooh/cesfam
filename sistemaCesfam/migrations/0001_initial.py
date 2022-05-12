# Generated by Django 4.0.4 on 2022-05-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('stock', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meds_Entregados',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('receta_id', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('rut', models.IntegerField()),
                ('digitoVer', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('celular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('rut', models.IntegerField()),
                ('digitoVer', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('contra', models.CharField(max_length=50)),
                ('tipoUsuario', models.CharField(max_length=50)),
            ],
        ),
    ]