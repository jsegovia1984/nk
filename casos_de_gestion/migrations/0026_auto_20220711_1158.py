# Generated by Django 3.1.7 on 2022-07-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0016_auto_20211118_1527'),
        ('casos_de_gestion', '0025_auto_20211118_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='lugar_operativo',
            field=models.ForeignKey(blank=True, db_column='lugar', limit_choices_to={'vigente': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='agenda.agenda', to_field='lugar'),
        ),
    ]
