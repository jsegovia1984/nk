# Generated by Django 3.1.7 on 2021-04-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='centros',
            name='CUIT',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
