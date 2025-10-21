from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def home(request): #request argument has to be here
    context= { #Dictionary that has a dictionary with posts
        'posts': Post.objects.all() #key names should be the same as the dictionary key field names
    }
    return render(request, 'blog/home.html', context) #will let us access "context" dictionary.
    #return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'}) #can do context directly here(dict)

