# Generated by Django 4.2.5 on 2023-09-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='number_phone',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
    ]
