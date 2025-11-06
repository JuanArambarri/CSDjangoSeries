from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics') #profile_pics is a directory
    ###Cascade -> if user is deleted, profile is also deleted. If profile is deleted, user is not.

    def __str__(self):
        return f'{self.user.username} Profile'

# Create your models here.
    def save(self): #run after our model is saved
        super().save() #run parent save
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

