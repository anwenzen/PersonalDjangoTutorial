from django.urls import path
from . import views

app_name = 'bolg'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.About.as_view(), name='about'),
    path('post.html', views.post, name='post'),
    path('contact.html', views.Contact.as_view(), name='contact'),
    path('show/<str:paper_name>', views.show_post, name='show_paper'),
]