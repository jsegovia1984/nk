# Generated by Django 3.1.7 on 2021-06-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0008_auto_20210615_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadricula',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='prestador',
            field=models.CharField(blank=True, choices=[('SPUB', 'Salud Publica'), ('SPRI', 'Salud Privada'), ('PAMI', 'PAMI'), ('IOMA', 'IOMA'), ('INCL', 'INCLUIR'), ('OTRA', 'OTRA')], max_length=4, null=True),
        ),
    ]
