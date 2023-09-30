from django.urls import path
from .views import profile_view, login_view, logout_view, register_view, add_vacation


urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('advertisement-add-vacation/', add_vacation, name='add-vacation'),
]