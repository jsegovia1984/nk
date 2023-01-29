# Generated by Django 3.1.7 on 2021-04-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0010_prestadoresdeprimernivel_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico_por_imagenes',
            name='capita',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ecodoppler',
            name='capita',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='kinesiologia',
            name='capita',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='prestadoresdeprimernivel',
            name='capita',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]