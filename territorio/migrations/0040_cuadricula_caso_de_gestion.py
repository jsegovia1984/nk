# Generated by Django 3.1.7 on 2021-08-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0039_auto_20210823_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadricula',
            name='caso_de_gestion',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='¿hay un caso de gestion a resolver?'),
        ),
    ]