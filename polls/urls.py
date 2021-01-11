from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_subjects),
    path('teachers/', views.show_teachers),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login/', views.login),
    path('get_captcha/', views.get_captcha),
    path('logout/', views.logout),
    path('test', views.test),
    path('excel/', views.export_teachers_excel),
    path('pdf/', views.export_pdf),
    path('teachers_data/', views.get_teachers_data),
    path('data/', views.teacher_data),
]
