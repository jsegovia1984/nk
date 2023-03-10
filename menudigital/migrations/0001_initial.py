# Generated by Django 3.1.7 on 2023-01-16 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sucursal', models.IntegerField()),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('barrio', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='postres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('porcion', models.IntegerField(blank=True, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('descuento', models.IntegerField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion', models.CharField(blank=True, max_length=50, null=True)),
                ('disponible', models.BooleanField(blank=True, null=True)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menudigital.lugar')),
            ],
        ),
    ]
