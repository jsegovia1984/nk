# Generated by Django 3.1.7 on 2021-06-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos_de_gestion', '0011_auto_20210627_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='casos',
            name='geo_parcial',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
