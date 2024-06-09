from django.shortcuts import render

# Create your views here.
def myHomeView(*args, **kwargs):
    return HttpResponse('<h1> Hola mundo desde Django</h1>')