from django.urls import reverse_lazy
from .forms import CustomUserRegister
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Resume, Vacancy
from .forms import VacancyForm, ResumeForm
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'app_auth/index.html', context)


def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegister(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            form.save()
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)
            login(request, user=user)
            return redirect(reverse('profile'))
        return render(request, 'app_auth/register.html', {'form': form})
    form = CustomUserRegister()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    return redirect(reverse('app_auth/login.html', {'error': 'пользователь не найден'}))


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    user = request.user
    resumes = Resume.objects.filter(user=user)
    return render(request, 'app_auth/profile.html', {'resumes': resumes})



def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required(login_url=reverse_lazy('login'))
def add_vacation(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacation = form.save(commit=False)
            vacation.user = request.user
            vacation.save()
            return redirect(reverse('index-page'))
        return render(request, 'app_auth/add_vacation.html', {'form': form})
    form = VacancyForm()
    return render(request, 'app_auth/add_vacation.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
def add_resume(request, pk):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.vacation_id = pk
            resume.user = request.user
            resume.save()
            return redirect(reverse('index-page'))
        return render(request, 'app_auth/resume.html', {'form': form})
    form = ResumeForm()
    return render(request, 'app_auth/resume.html', {'form': form})