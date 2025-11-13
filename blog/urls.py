from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views #. imports from this folder

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #empty path is homepage, path naming avoids confusion
    path('about/',views.about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #int:pk requests an int posting key
]
