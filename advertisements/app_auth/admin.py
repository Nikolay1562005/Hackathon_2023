from django.contrib import admin
from .models import Vacancy, Resume


class VacancyAdmin(admin.ModelAdmin):

    list_display = ['name_vacancy', 'description', 'salary', 'organization']


admin.site.register(Vacancy, VacancyAdmin)



class ResumeAdmin(admin.ModelAdmin):

    list_display = ['user', 'commentary', 'resume', 'number_phone']


admin.site.register(Resume, ResumeAdmin)