# Generated by Django 3.1.7 on 2021-06-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0009_auto_20210615_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadricula',
            name='conoces_la_linea_144',
            field=models.BooleanField(blank=True, help_text='Existe el programa, el cual buscar fortalecer economicamente a las victimas que sufren violencia de genero', null=True),
        ),
    ]
