# Generated by Django 3.1.7 on 2021-08-31 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_auto_20210830_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='dias',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
