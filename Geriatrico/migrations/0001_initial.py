# Generated by Django 3.1.7 on 2021-04-05 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestadores', '0012_resonancia_magnetica_tomografia_computada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geriatrico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(choices=[('E', 'RAM'), ('N', 'RAMP')], max_length=1)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad_de_afiliados', models.CharField(blank=True, max_length=20, null=True)),
                ('conveniado', models.BooleanField(default=True)),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestadores.localidad')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestadores.municipio')),
            ],
            options={
                'verbose_name': 'Geriatrico',
                'verbose_name_plural': 'Geriatricos',
            },
        ),
    ]