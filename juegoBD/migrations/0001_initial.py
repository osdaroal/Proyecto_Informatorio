# Generated by Django 3.2.6 on 2021-08-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Definición')),
                ('categoria', models.CharField(max_length=30, verbose_name='categoía de la pregunta')),
                ('letra', models.CharField(max_length=1, verbose_name='letra en el rosco')),
                ('respuesta', models.CharField(max_length=60, verbose_name='respuesta')),
            ],
        ),
    ]
