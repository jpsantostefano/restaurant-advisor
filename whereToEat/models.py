from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

#This is what I see in admin
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    

    def __str__(self):
        return self.title