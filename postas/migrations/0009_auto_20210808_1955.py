# Generated by Django 3.1.7 on 2021-08-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postas', '0008_auto_20210808_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='horario_ingreso',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='horario_salida',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
