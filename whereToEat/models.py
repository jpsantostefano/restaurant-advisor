from django.db import models
from django.contrib.auth.models import User



#This is what I see in admin
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return '%s - %s' % (self.name)

    class Meta:
        ordering = ['date_added']