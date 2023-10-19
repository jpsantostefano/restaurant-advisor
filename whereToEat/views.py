from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


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


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {'form':form}
    return render(request, 'registration/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfull logout')
    return redirect('index')