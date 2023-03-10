# Generated by Django 3.1.7 on 2021-04-06 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Geriatrico', '0002_auto_20210405_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_de_facturacion', models.DateField()),
                ('Monto', models.FloatField(blank=True, null=True)),
                ('Lugar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Geriatrico.geriatrico')),
            ],
            options={
                'verbose_name': 'Facturacion',
                'verbose_name_plural': 'Facturacion',
            },
        ),
    ]
