# Generated by Django 3.1.7 on 2021-06-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0023_auto_20210617_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadricula',
            name='beneficios',
            field=models.ManyToManyField(help_text='Recordar que mayores de 60 (mujeres) y 65 (hombres) con algunos años de aportes se pueden jubilar, Si tiene hijxs puede cobrar AUH (Si no estan registradxs lxs progenitorxs) y Suaf (Si estan registradxs)', to='territorio.beneficios_anses'),
        ),
    ]
