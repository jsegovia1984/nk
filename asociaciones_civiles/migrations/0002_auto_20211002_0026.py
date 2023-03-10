# Generated by Django 3.1.7 on 2021-10-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asociaciones_civiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proceso',
            options={'verbose_name': 'Proceso', 'verbose_name_plural': 'Procesos'},
        ),
        migrations.AlterModelOptions(
            name='situacion_documental',
            options={'verbose_name': 'Situacion Documental', 'verbose_name_plural': 'Situaciones Documentales'},
        ),
        migrations.AlterModelOptions(
            name='tipo_ac',
            options={'verbose_name': 'Tipo de Asociacion civil', 'verbose_name_plural': 'Tipos de Asociaciones civiles'},
        ),
        migrations.AlterField(
            model_name='asociaciones_civiles',
            name='direccion',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='asociaciones_civiles',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
