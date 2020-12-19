"""PersonalDjangoTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import PersonalDjangoTutorial.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PersonalDjangoTutorial.views.index),
    path('pscp/', PersonalDjangoTutorial.views.pscp),
    path('downloads/', PersonalDjangoTutorial.views.downloads),
    path('404/', PersonalDjangoTutorial.views.not_found),
    path('download_m3u8', PersonalDjangoTutorial.views.m3u8_downloads),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('spider/', include('spider.urls')),
]

handler404 = PersonalDjangoTutorial.views.page_not_found
