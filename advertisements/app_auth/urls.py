from django.urls import path
from .views import index, login_view, logout_view, register_view, add_vacation, profile_view, add_resume


urlpatterns = [
    path('', index, name='index-page'),
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('add-vacation/', add_vacation, name='add-vacation'),
    path('resume/<int:pk>', add_resume, name='resume')
]