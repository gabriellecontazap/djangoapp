# Generated by Django 3.1 on 2020-09-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armarios_system', '0005_coluna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coluna',
            name='componentes',
            field=models.CharField(max_length=1000),
        ),
    ]