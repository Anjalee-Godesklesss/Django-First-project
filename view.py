
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("ths is first project")

def demo(request):
    return HttpResponse("please subscribe the channel")
