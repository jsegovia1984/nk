# Generated by Django 3.1.7 on 2021-10-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos_de_gestion', '0019_auto_20211029_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='fecha_de_entrada',
            field=models.DateField(default='2021-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='casos',
            name='metodo_de_entrada',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]