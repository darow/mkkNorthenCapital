from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('registration/', views.registration),
    path('setcookie/', views.setcookie),
    path('showcookie/', views.showcookie)
]