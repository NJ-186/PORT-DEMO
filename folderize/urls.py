from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('/add_video', views.add_video, name = 'add_video'),
    path('/add_folder', views.add_folder, name = 'add_folder'),
    path('/move_video', views.move_video, name = 'move_video'),
]