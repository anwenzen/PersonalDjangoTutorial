from django.urls import path
from . import views

app_name = 'bolg'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('index.html', views.Index.as_view(), name='index'),
    path('about.html', views.About.as_view(), name='about'),
    path('post.html', views.post, name='post'),
    path('contact.html', views.Contact.as_view(), name='contact'),
]