# Generated by Django 3.1.7 on 2021-06-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos_de_gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casos',
            name='region',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]