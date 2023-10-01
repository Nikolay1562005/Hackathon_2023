from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()

class Vacancy(models.Model):
    name_vacancy = models.CharField("Название вакансии", max_length=128)
    description = models.TextField('Описание')
    create_at = models.DateTimeField("Время создания", auto_now_add=True)
    salary = models.IntegerField("З/П (руб.месяц)")
    organization = models.CharField("Организация", max_length=255, blank=False)
    def get_url(self):
        return reverse('resume', kwargs={'pk': self.pk})


class Resume(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    commentary = models.TextField("Комментарий", blank=True)
    resume = models.ImageField("Резюме", upload_to='resumes/')
    number_phone = models.CharField("Номер телефона", max_length=12)
    is_answered = models.BooleanField(default=False)
    vacation_id = models.IntegerField("ID вакансии")