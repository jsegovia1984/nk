# Generated by Django 3.1.7 on 2021-07-07 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0031_auto_20210707_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadricula',
            name='preferencia',
            field=models.CharField(blank=True, choices=[('FT', 'Frente de Todxs'), ('JXC', 'Juntos por el Cambio'), ('AL', 'Avanza Libertad'), ('CF', 'Consenso Federal'), ('FIT', 'Frente de Izquierda'), ('NOS', 'Nos'), ('OTR', 'Otro'), ('NIN', 'Ninguno')], max_length=3, null=True, verbose_name='¿Se refencia con algún partido político?¿Cuál?'),
        ),
    ]
