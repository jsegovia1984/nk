# Generated by Django 3.1.7 on 2021-10-22 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cronos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aranceles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cronos.modalidad')),
            ],
            options={
                'verbose_name': 'Arancel',
                'verbose_name_plural': 'Aranceles',
            },
        ),
    ]
