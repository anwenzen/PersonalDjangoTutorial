
from django.shortcuts import render, redirect
from django.views import generic
from .models import Paper, Message

# Create your views here.


class Index(generic.TemplateView):
    paper_list = Paper.objects.all()
    template_name = 'blog/index.html'


def index(request):
    return render(request, 'blog/index.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get("email")
        print(name, password, email)
    return render(request, 'blog/registration.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')
        print(name, passwd)
    return render(request, 'blog/login.html')


def logout(request):
    request.session.flush()
    return redirect('/blog/index')


def post(request):
    return render(request, 'blog/blog-post.html')


def post_list(request):
    return render(request, 'blog/blog-post-list.html')


def contact(request):
    if request.method == "POST":
        Message.objects.get_or_create(name=request.POST.get('name'),
                                      message=request.POST.get('message'))
        return redirect('/blog/contact')
    return render(request, 'blog/contact-us.html', {'message': Message.objects.all()})


def code_test(request):
    return render(request, 'blog/test.html')
