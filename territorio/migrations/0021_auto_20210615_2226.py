# Generated by Django 3.1.7 on 2021-06-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0020_auto_20210615_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadricula',
            name='DNI',
            field=models.BooleanField(blank=True, null=True, verbose_name='¿Tiene actualmente DNI?'),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='conoces_la_linea_144',
            field=models.BooleanField(blank=True, help_text='Existe el programa ACOMPAÑAR, el cual buscar fortalecer economicamente a las victimas que sufren violencia de genero', null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='prestacion_alinentaria',
            field=models.BooleanField(blank=True, help_text='¿Reciben prestacion alimentaria o asisten a algun comedor o merendero?', null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='tuvo_DNI_alguna_vez',
            field=models.BooleanField(blank=True, null=True, verbose_name='¿Tuvo alguna vez DNI?'),
        ),
    ]
