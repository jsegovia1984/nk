# Generated by Django 3.1.7 on 2021-06-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0021_auto_20210615_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadricula',
            name='cobran_correctamente',
            field=models.BooleanField(blank=True, help_text='¿Cobran las prestaciones de ANSES correctamente?', null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='desea_inscribirse',
            field=models.BooleanField(blank=True, help_text='Comentar sobre la mesa de Vacunate', null=True, verbose_name='¿Desea Inscribirse?'),
        ),
    ]
