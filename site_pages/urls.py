from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('registration/', views.registration),
    path('ques_ans/', views.ques_ans),
    path('about_us/', views.about_us),
]