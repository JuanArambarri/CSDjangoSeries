from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) ### Allows to modify/create new posts from the admin page
