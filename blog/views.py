from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Juan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 16, 2025'
    },
    {
        'author': 'Fer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 17, 2025'
    }
]

# Create your views here.
def home(request): #request argument has to be here
    context= { #Dictionary that has a dictionary with posts
        'posts': posts
    }
    return render(request, 'blog/home.html', context) #will let us access "context" dictionary.
    #return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'}) #can do context directly here(dict)

