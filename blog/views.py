from django.shortcuts import render
from django.views import generic
from .models import Paper

# Create your views here.


class Index(generic.TemplateView):
    paper_list = Paper.objects.all()
    template_name = 'blog/index.html'


def index(request):
    paper_list = Paper.objects.all()
    return render(request, 'blog/index.html', {'paper_list': paper_list[:10:-1]})


def login(requests):
    return render(requests, 'blog/login.html')


def paper(request, paper_id):
    if paper_id:
        pass
    return render(request, 'blog/post.html', {})


def post(request):
    if request.method == "GET":
        return render(request, 'blog/post.html')
    if request.method == "POST":
        sub_paper = Paper(title=request.POST['title'],
                          details=request.POST['paper'][:100],
                          content=request.POST['paper'],
                          date=request.POST['date'],
                          author=request.POST['author']
                          )
        sub_paper.save()
        return render(request, 'blog/post.html')


def show_post(request, paper_name):
    one_of_paper = Paper.objects.get(title=paper_name)
    return render(request, 'blog/show_post.html', {'paper': one_of_paper})
