# Generated by Django 3.1.7 on 2021-10-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_auto_20211027_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='lugar',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
