# Generated by Django 3.1.7 on 2022-03-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migraciones', '0005_auto_20211031_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
