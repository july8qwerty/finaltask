from django.urls import path
from . import views



urlpatterns = [

    path('', views.demo, name='demo'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]
