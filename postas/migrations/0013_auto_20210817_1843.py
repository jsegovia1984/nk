# Generated by Django 3.1.7 on 2021-08-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postas', '0012_conteo_de_vacunas'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteo_de_vacunas',
            name='cantidad_turnera',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conteo_de_vacunas',
            name='turnera',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
