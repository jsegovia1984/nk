# Generated by Django 3.1.7 on 2021-06-14 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0020_auto_20210614_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odontologia_primaria',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prestadores.localidad'),
        ),
        migrations.AlterField(
            model_name='odontologia_primaria',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prestadores.municipio'),
        ),
    ]
