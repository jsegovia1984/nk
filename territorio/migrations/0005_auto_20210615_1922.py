# Generated by Django 3.1.7 on 2021-06-15 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0004_cuadricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuadricula',
            old_name='cobran_prestaciones_de_anses_correctamente',
            new_name='cobran_correctamente',
        ),
    ]
