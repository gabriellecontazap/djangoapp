# Generated by Django 3.1 on 2020-09-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armarios_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]