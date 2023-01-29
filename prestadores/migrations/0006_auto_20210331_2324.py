# Generated by Django 3.1.7 on 2021-03-31 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0005_diagnostico_por_imagenes_ecodoppler_kinesiologia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestadores.localidad')),
            ],
            options={
                'verbose_name': 'Agencia',
                'verbose_name_plural': 'Agencias',
            },
        ),
        migrations.AddField(
            model_name='prestadoresdeprimernivel',
            name='agencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestadores.agencia'),
        ),
    ]