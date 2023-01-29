# Generated by Django 3.1.7 on 2021-06-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0026_auto_20210617_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadricula',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='preferencia',
            field=models.CharField(blank=True, choices=[('FT', 'Frente de Todxs'), ('JXC', 'Juntos por el Cambio'), ('AL', 'Avanza Libertad'), ('CF', 'Consenso Federal'), ('FIT', 'Frente de Izquierda'), ('NOS', 'NOS'), ('OTR', 'OTRO')], max_length=3, null=True, verbose_name='¿Se refencia con algún partido político?¿Cuál?'),
        ),
    ]