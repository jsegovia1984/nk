# Generated by Django 3.1.7 on 2021-04-21 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0002_centros_cuit'),
    ]

    operations = [
        migrations.AddField(
            model_name='centros',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='centros',
            name='personeria_Juridica',
            field=models.CharField(choices=[('R', 'Regularizar/Normalizar'), ('C', 'Construir'), ('T', 'En Tramite'), ('N', 'No Tiene')], default='R', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centros',
            name='relacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='centros',
            name='sap',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='centros',
            name='subsidio',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Subsidios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('descipcion', models.TextField(blank=True, max_length=50, null=True)),
                ('centro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='centros.centros')),
            ],
            options={
                'verbose_name': 'subsidio',
                'verbose_name_plural': 'subsidios',
            },
        ),
    ]
