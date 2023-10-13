from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
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
