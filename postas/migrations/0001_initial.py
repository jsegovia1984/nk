# Generated by Django 3.1.7 on 2021-08-07 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('territorio', '0037_auto_20210803_1831'),
        ('prestadores', '0021_auto_20210614_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='postas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prestadores.localidad')),
            ],
            options={
                'verbose_name': 'posta',
                'verbose_name_plural': 'postas',
            },
        ),
        migrations.CreateModel(
            name='becarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.TextField(blank=True, null=True)),
                ('tarea', models.TextField(blank=True, null=True)),
                ('carga_horaria', models.CharField(blank=True, max_length=50, null=True)),
                ('organizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='territorio.organizacion')),
            ],
            options={
                'verbose_name': 'Becario',
                'verbose_name_plural': 'Becarios',
            },
        ),
    ]