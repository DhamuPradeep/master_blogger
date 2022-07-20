from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from PIL import Image
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,default=None)
    body = models.CharField(max_length=1000000,default=None)
    user = models.TextField(default=None)
    image = models.ImageField(upload_to='images/',height_field=None, width_field=None, max_length=100,default=None,blank=True,null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True,null=True)

    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path) # Open image using self
        if img.height > 300 or img.width > 300:
            new_img = (500,500)
            img.thumbnail(new_img)
            img.save(self.image.path)


