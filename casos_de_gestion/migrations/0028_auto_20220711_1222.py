# Generated by Django 3.1.7 on 2022-07-11 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casos_de_gestion', '0027_auto_20220711_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='organismo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='casos_de_gestion.organismo'),
        ),
    ]