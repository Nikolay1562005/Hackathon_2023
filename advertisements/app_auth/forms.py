from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vacancy

from django import forms


class CustomUserRegister(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']

class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['name_vacancy', 'description', 'salary', 'organization']
        # widgets = {
        #     'name_vacancy': forms.CharField(attrs={'class': 'form-control form-control-lg'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        #     'salary': forms.IntegerField(attrs={'class': 'form-control form-control-lg'}),
        #     'organization': forms.Textarea(attrs={'class': 'form-control form-control-lg'})
        # }