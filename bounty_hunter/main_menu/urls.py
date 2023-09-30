from django.urls import path
import views


urlpatterns = [
    path('', views.index, name='main-page'),
    path('login', views.login, name='login-page')
]