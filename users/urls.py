from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_, name='logout')
]