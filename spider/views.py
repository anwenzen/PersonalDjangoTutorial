import random
import time
from requests import Session

from lxml import etree
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'spider/index.html')



