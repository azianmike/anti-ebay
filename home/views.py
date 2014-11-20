from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the home index.")
    return render_to_response('index.html')   
    #template = loader.get_template("index.html")
    #return HttpResponse(template.render())

