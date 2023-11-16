from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name','last_name', 'instagram', 'image']

#         labels = {
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'instagram':'Instagram',
#             'image':'Profile Picture',
#         }