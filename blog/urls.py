from django.urls import path
from . import views #. imports from this folder

urlpatterns = [
    path('', views.home, name='blog-home'), #empty path is homepage, path naming avoids confusion
    path('about/',views.about, name='blog-about'),
]