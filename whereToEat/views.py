from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import Template, Context
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic, View
from .forms import CommentForm
from .models import Comment


# Create your views here.


def index(request):
    #Open the document
    index = open("templates/index.html")
    #Load the document
    template = Template(index.read())
    #Close the document
    index.close()
    #Create a context
    context = Context()
    #Rendering the document
    document = template.render(context)
    return HttpResponse(document)

def prueba(request):
    #Open the document
    prueba = open("templates/prueba.html")
    #Load the document
    template = Template(prueba.read())
    #Close the document
    prueba.close()
    #Create a context
    context = Context()
    #Rendering the document
    document = template.render(context)
    return HttpResponse(document)

def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Asigna el usuario actual al comentario
            comment.post_id = post_id    # Asigna el post al comentario
            comment.save()
            return redirect('prueba', post_id=post_id)  # Redirige a la página de detalles del post
    else:
        form = CommentForm()
    return render(request, 'prueba', {'form': form})


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('registration/register.html')

        myuser = User.objects.create_user(username=username, email=email, password=password)
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
            return render(request, 'index.html')
        else:
            messages.error(request, 'Bad Credentials!')
            return redirect("index")
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfull logout')
    return redirect('index')