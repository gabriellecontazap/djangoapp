# Generated by Django 3.1 on 2020-09-02 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armarios_system', '0002_obra_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armario',
            name='obra',
            field=models.IntegerField(),
        ),
    ]