# Generated by Django 3.1.7 on 2021-10-28 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20211028_1008'),
        ('casos_de_gestion', '0016_casos_lugar_operativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='lugar_operativo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='agenda.agenda', to_field='lugar'),
        ),
    ]
