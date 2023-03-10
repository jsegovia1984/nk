# Generated by Django 3.1.7 on 2021-06-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organismo', models.CharField(choices=[('SUB', 'Subsecreatria de DDHH'), ('PAM', 'PAMI'), ('COE', 'Consejo Escolar'), ('ANS', 'ANSES'), ('ACU', 'ACUMAR'), ('REN', 'RENAPER'), ('MIG', 'Migraciones')], max_length=3)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]
