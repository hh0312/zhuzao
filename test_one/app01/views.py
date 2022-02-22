from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index_test(request):
    return HttpResponse("欢迎使用")


def index(request):
    return render(request, 'index1.html')


def test(request):
    return render(request, 'test.html')
