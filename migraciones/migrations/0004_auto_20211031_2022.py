# Generated by Django 3.1.7 on 2021-10-31 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migraciones', '0003_auto_20210923_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='casos',
            name='nacionalidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='migraciones.nacionalidad'),
        ),
    ]
