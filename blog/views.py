from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): #request argument has to be here
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

