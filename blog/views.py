from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse

# Create your views here.
def home(request): #request argument has to be here
    context= { #Dictionary that has a dictionary with posts
        'posts': Post.objects.all() #key names should be the same as the dictionary key field names
    }
    return render(request, 'blog/home.html', context) #will let us access "context" dictionary.
    #return HttpResponse('<h1>Blog Home</h1>')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #looking or <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #overwritten function
        form.instance.author = self.request.user #before requesting, check and validate instantiated user
        return super().form_valid(form) #runs the form valid on the parent class

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #overwritten function
        form.instance.author = self.request.user #before requesting, check and validate instantiated user
        return super().form_valid(form) #runs the form valid on the parent class

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html',{'title': 'About'}) #can do context directly here(dict)

