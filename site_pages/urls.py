from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('registration/', views.registration, name="registration"),
    path('create_customer_request/', views.create_customer_request, name="create_customer_request"),
    path('info/', views.info, name="info"),
    path('about_us/', views.about_us, name="about_us"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]