from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import Template, Context
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic, View
from .forms import CommentForm
from .models import Post, Comment, Profile
from django.db import models
from django import forms


# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password != password2:
            return redirect('register')

        myuser = User.objects.create_user(username=username, password=password)
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        return redirect('index')
    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('index')
        else:
            messages.error(request, "There was an error loggin in. Please try again")
    else:  
        return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('index')


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = request.user
            comment.save()
            messages.success(request, "You successfully left a comment!")

            return redirect('post_detail', slug=post.slug)
    else:
            form = CommentForm()
    return render(request, 'post_detail.html', {'post':post, 'form': form})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        if request.POST.get('confirm_delete'):
            comment.delete()
            messages.success(request, "You successfully deleted your comment!")
            return redirect('post_detail', slug=comment.post.slug)
    return render(request, 'delete_comment.html', {'comment': comment})
     

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully edited your comment!")
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form':form, 'comment':comment})

def profile_view(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, "profile_view.html", {"profile":profile})
    else:
        return redirect('index')

# def edit_profile(request):
#     user = request.user
#     profile = Profile.objects.get(user=user)

#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('profile_view')
#     else:
#         profile_form = ProfileForm(instance=profile)
#     return render(request, 'edit_profile.html',)