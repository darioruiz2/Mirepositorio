# Generated by Django 4.1.3 on 2022-11-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Fecha_nacimiento', models.CharField(max_length=50)),
            ],
        ),
    ]
