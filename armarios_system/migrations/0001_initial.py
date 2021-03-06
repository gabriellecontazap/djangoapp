# Generated by Django 3.1 on 2020-09-01 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor', models.CharField(max_length=255)),
                ('cliente', models.CharField(max_length=255)),
                ('deleted_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Armario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_flag', models.BooleanField(default=False)),
                ('obra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='armarios_system.obra')),
            ],
        ),
    ]
