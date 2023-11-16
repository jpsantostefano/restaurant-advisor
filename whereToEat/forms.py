from .models import Comment, Profile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','instagram', 'image']

