from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics') #profile_pics is a directory
    ###Cascade -> if user is deleted, profile is also deleted. If profile is deleted, user is not.

    def __str__(self):
        return f'{self.user.username} Profile'

# Create your models here.
