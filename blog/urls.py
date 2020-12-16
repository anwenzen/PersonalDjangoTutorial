from django.urls import path
from . import views

app_name = 'bolg'

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('post', views.post, name='post'),
    path('post-list', views.post_list, name='post-list'),
    path('registration', views.registration, name='registration'),
    path('contact', views.contact, name='contact'),
    path('test', views.test, name='test'),
    # path('show/<str:paper_name>', views.show_post, name='show_paper'),
]