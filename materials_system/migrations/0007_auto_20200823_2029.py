# Generated by Django 3.1 on 2020-08-23 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0006_auto_20200823_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cpf_cnpj', models.IntegerField()),
                ('deleted_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deleted_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Fabricantes',
            new_name='Fornecedores',
        ),
    ]