from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('all_feedback/', views.all_feedback, name='all_feedback'),
]

