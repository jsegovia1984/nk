# Generated by Django 3.1.7 on 2021-06-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos_de_gestion', '0007_casos_caso_resuelto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='caso_resuelto',
            field=models.BooleanField(default=True),
        ),
    ]
