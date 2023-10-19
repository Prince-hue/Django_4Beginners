from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Hello World')

def html_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html')