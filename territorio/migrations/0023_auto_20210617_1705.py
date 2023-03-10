# Generated by Django 3.1.7 on 2021-06-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0022_auto_20210615_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='beneficios_anses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Beneficio',
                'verbose_name_plural': 'Beneficios de Anses',
            },
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='discapacitados',
            field=models.BooleanField(blank=True, null=True, verbose_name='¿Hay alguna persona discapacitada?'),
        ),
        migrations.AddField(
            model_name='cuadricula',
            name='usuario',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
