from django.shortcuts import render
from django.views import generic
from .models import Paper

# Create your views here.


class Index(generic.TemplateView):
    template_name = 'blog/index.html'


class Contact(generic.TemplateView):
    template_name = 'blog/contact.html'


# class Post(generic.TemplateView):
#     template_name = 'blog/post.html'


class About(generic.TemplateView):
    template_name = 'blog/about.html'


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


def show_post(request):

    return render(request, )