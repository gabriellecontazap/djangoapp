# Generated by Django 3.1 on 2020-08-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0007_auto_20200823_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf_cnpj',
            field=models.CharField(max_length=255),
        ),
    ]
