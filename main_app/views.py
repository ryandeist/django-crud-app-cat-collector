from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Cat</h1>')

def about(request):
    return HttpResponse('<h1>About the CatCollector</h1>')
