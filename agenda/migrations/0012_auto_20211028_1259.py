# Generated by Django 3.1.7 on 2021-10-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20211028_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='lugar',
            field=models.CharField(blank=True, db_column='lugar', max_length=50, unique=True),
        ),
    ]
