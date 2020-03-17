from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('connection/', views.FilteredConnectionListView.as_view(), name='connection'),
    path('connection/create/', views.connection_create, name='connection_create'),
    path('task/', views.FilteredTaskListView.as_view(), name='task'),
    path('task/create/', views.task_create, name='task_create'),
]
