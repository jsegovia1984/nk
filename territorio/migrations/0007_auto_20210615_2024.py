# Generated by Django 3.1.7 on 2021-06-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0006_auto_20210615_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadricula',
            name='DNI',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='Tuvo_DNI',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='nacionalidad',
            field=models.CharField(blank=True, choices=[('ARG', 'ARGENTINX'), ('BOL', 'BOLIVINX'), ('URU', 'URUGUAYX'), ('PAR', 'PARAGUAYX'), ('BRA', 'BRASILERX'), ('CHI', 'CHILENX'), ('OTRO', 'OTRX')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='apellido',
            field=models.CharField(default='True', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='nombre',
            field=models.CharField(default='rue', max_length=50),
            preserve_default=False,
        ),
    ]
