# Generated by Django 3.1.7 on 2021-10-01 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestadores', '0021_auto_20210614_1414'),
        ('territorio', '0040_cuadricula_caso_de_gestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='situacion_documental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_ac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='asociaciones_civiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('grado_de_relacion', models.CharField(blank=True, max_length=30, null=True)),
                ('Inscripta', models.BooleanField(default=True)),
                ('numero', models.CharField(blank=True, max_length=25, null=True)),
                ('situacion_documental', models.CharField(blank=True, max_length=40, null=True)),
                ('proceso', models.CharField(blank=True, max_length=40, null=True)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('recursos_y_actividades', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('geo_parcial', models.BooleanField(blank=True, default=False, null=True)),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prestadores.localidad')),
                ('organizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='territorio.organizacion')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='asociaciones_civiles.tipo_ac')),
            ],
            options={
                'verbose_name': 'Asociacion civil',
                'verbose_name_plural': 'Asociciones civiles',
            },
        ),
    ]
