from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save




#This is what I see in admin
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __self__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['date_added']



#new
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField()
    last_name = models.CharField()
    instagram = models.CharField()
    email = models.EmailField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username

# Create Profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)


