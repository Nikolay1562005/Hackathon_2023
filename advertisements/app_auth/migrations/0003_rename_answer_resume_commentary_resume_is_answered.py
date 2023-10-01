# Generated by Django 4.2.5 on 2023-09-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0002_alter_resume_number_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='answer',
            new_name='commentary',
        ),
        migrations.AddField(
            model_name='resume',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
    ]