from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['name_vacancy', 'description', 'salary', 'organization']



admin.site.register(Vacancy, VacancyAdmin)