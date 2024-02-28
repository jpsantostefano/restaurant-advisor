from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import Template, Context
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic, View
from .forms import CommentForm, ProfileForm
from .models import Post, Comment, Profile
from django.db import models
from django import forms

# Create your views here

# Home view
def index(request):
    # Shows all the posts
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


# Sign Up view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            message.alert(request, "You're typing a different password.")
            return redirect('register')
        # Saves the user information
        myuser = User.objects.create_user(username=username, password=password)
        myuser.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Your Account has been successfully created.")
        return redirect('index')
    return render(request, 'registration/register.html')


# Sign in/ out view:

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
            messages.error(request, "There was an error loggin in. Please try again.")
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def logout_view(request):
    # Logout the user
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')


# Post views
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    # Comment form
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
    return render(request, 'post_detail.html', {'post': post, 'form': form})


# Comment views
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        if request.POST.get('confirm_delete'):
            comment.delete()
            messages.success(request, "You successfully deleted your comment!")
            return redirect('post_detail', slug=comment.post.slug)
    return render(request, 'delete_comment.html', {'comment': comment})


def edit_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id)
        # Edit comment form
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, "You successfully edited your comment!")
                return redirect('post_detail', slug=comment.post.slug)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})
    else:
        messages.error(request, "You must be logged in to see this page.")
        return redirect('index')


# Profile views:
def profile_view(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'profile_view.html', {'profile': profile})
    else:
        return redirect('index')


def edit_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        print(profile)
        # Verify if the user is the ownwer of the profile
        if request.user == profile.user:
            if request.method == 'POST':
                # Process data
                form = ProfileForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, "You successfully edited your profile!")
                    return redirect('profile_view', pk=pk)
            else:
                # If it's a GET request, shows the edition form.
                form = ProfileForm(instance=profile)
            return render(request, 'edit_profile.html', {'form': form})
        else:
            # If the user is not permited to see this page.
            messages.error(request, "You don't have permission to edit this profile.")
            return redirect('index')
    else:
        messages.error(request, "You must be logged in to see this page.")
        return redirect('index')
