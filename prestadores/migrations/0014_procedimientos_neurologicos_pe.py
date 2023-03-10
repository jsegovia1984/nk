# Generated by Django 3.1.7 on 2021-04-06 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0013_artroscopia_cardiologia_alta_complejidad_y_hemodinamia_cirugia_cardiovascular_colocacion_de_marcapas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimientos_neurologicos_pe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(blank=True, max_length=50, null=True)),
                ('capita', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestadores.localidad')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestadores.municipio')),
            ],
            options={
                'verbose_name': 'Procedimientos neurologico PE',
                'verbose_name_plural': 'Procedimientos neurologicos PE',
            },
        ),
    ]
