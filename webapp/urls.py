from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('connections/', views.connection_filtered, name='connection_filtered'),
    path('connection/', views.FilteredConnectionListView.as_view(), name='connection'),
    path('connection/create/', views.connection_create, name='connection_create'),
    path('task/', views.task, name='task'),
]
