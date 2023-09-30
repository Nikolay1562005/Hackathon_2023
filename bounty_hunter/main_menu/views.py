from django.shortcuts import render

def index(request):
    context = {'main_page_context': ''}
    return render(request, 'main_menu\main-page.html', context)