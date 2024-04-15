from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('trainers/', views.Trainers.as_view(), name='trainers'),
    path('trainer/<slug:slug>', views.TrainerView.as_view(), name='trainer'),
]