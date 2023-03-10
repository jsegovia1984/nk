# Generated by Django 3.1.7 on 2021-11-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronos', '0009_auto_20211104_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastos',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gastos',
            name='precio_unitario',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gastos',
            name='unidades',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='precio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
