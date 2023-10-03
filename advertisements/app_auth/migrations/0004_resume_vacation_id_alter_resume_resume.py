# Generated by Django 4.2.5 on 2023-10-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_rename_answer_resume_commentary_resume_is_answered'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='vacation_id',
            field=models.IntegerField(default=1, verbose_name='ID вакансии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.ImageField(upload_to='resumes/', verbose_name='Резюме'),
        ),
    ]
