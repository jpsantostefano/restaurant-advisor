from .models import Comment, Profile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            'class': 'textarea',
        })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'instagram', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':
                                                      'login-register-input'})
        self.fields['last_name'].widget.attrs.update({'class':
                                                      'login-register-input'})
        self.fields['email'].widget.attrs.update({'class':
                                                  'login-register-input'})
        self.fields['instagram'].widget.attrs.update({'class':
                                                     'login-register-input'})