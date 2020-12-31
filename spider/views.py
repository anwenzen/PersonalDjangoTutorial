from django.shortcuts import render, redirect

from .lagou_spider import Spider
# Create your views here.
from .models import Position


def index(request):
    hint = None
    if 'hint' in request.GET:
        hint = 'done'
    position = Position.objects.all()
    return render(request, 'spider/spider.html', {'position': position, 'hint': hint})


def spider_data(request):
    if request.method == "POST":
        key_word = request.POST.get('key_word')
        Spider(key_word=key_word).main()
    return redirect('/spider/index?hint=done')


def position_data_preview(request):
    if request.method == "POST":
        if 'key_word' in request.POST:
            key_word = request.POST.get('key_word')
            position_data = Position.objects.get()
            return render(request, 'spider/position_preview.html', {'position_data': position_data})
    return render(request, 'spider/position_preview.html', {'position_data': ''})
