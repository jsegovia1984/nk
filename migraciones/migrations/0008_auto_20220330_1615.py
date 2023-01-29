# Generated by Django 3.1.7 on 2022-03-30 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0021_auto_20210614_1414'),
        ('migraciones', '0007_casos_interministerial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='agente',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='casos',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casos',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casos',
            name='dni_cedula',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='casos',
            name='estado_del_tramite',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casos',
            name='expediente',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='casos',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='casos',
            name='fecha_de_toma',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='casos',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CasosMigraciones', to='prestadores.localidad'),
        ),
        migrations.AlterField(
            model_name='casos',
            name='lugar_de_toma',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casos',
            name='modo_de_toma',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casos',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='migraciones.nacionalidad'),
        ),
        migrations.AlterField(
            model_name='casos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casos',
            name='telefono',
            field=models.CharField(max_length=30),
        ),
    ]
