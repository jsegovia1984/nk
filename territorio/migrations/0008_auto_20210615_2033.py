# Generated by Django 3.1.7 on 2021-06-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0007_auto_20210615_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuadricula',
            name='Tuvo_DNI',
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='conoces_la_linea_144',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='prestacion_alinentaria',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='tuvo_DNI_alguna_vez',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='DNI',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='cobertura_de_salud',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='cobran_correctamente',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='desea_inscribirse',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='inscriptx_vacuna',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuadricula',
            name='nacionalidad',
            field=models.CharField(blank=True, choices=[('ARG', 'ARGENTINO/A'), ('BOL', 'BOLIVINO/A'), ('URU', 'URUGUAYO/A'), ('PAR', 'PARAGUAYO/A'), ('BRA', 'BRASILERO/A'), ('CHI', 'CHILENO/A'), ('OTRO', 'OTRX')], max_length=4, null=True),
        ),
    ]
