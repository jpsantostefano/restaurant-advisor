from .models import CustomUser
from django import forms


class CustomUserCreationForm(forms.ModelForm):
     class Meta:
        model = CustomUser
        fields = ['username','password']