# Generated by Django 3.1.7 on 2021-06-15 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0014_auto_20210615_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadricula',
            name='cobertura_de_salud',
            field=models.BooleanField(blank=True, null=True, verbose_name='Tiene Cobertura de salud'),
        ),
    ]
