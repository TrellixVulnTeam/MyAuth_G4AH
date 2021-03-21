from django.urls import include, path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
]
