from django.urls import path
from webapp import views
from webapp import forms

urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
]
