# Generated by Django 3.1.7 on 2021-09-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos_de_gestion', '0013_casos_interministerial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='tipo_de_Tramite',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
