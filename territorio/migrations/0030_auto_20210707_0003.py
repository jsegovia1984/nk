# Generated by Django 3.1.7 on 2021-07-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0029_cuadricula_trabajo_registrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadricula',
            name='preferencia',
            field=models.CharField(blank=True, choices=[('FT', 'Frente de Todxs'), ('JXC', 'Juntos por el Cambio'), ('AL', 'Avanza Libertad'), ('CF', 'Consenso Federal'), ('FIT', 'Frente de Izquierda'), ('NOS', 'NOS'), ('NIN', 'NINGUNO'), ('OTR', 'OTRO')], max_length=3, null=True, verbose_name='¿Se refencia con algún partido político?¿Cuál?'),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='prestador',
            field=models.CharField(blank=True, choices=[('SPRI', 'Salud Privada'), ('PAMI', 'PAMI'), ('IOMA', 'IOMA'), ('INCL', 'INCLUIR'), ('OTRA', 'OTRA')], max_length=4, null=True),
        ),
    ]
