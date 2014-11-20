from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'login.html',{})
    #return HttpResponse("Hello, world. You're at the login index.")


