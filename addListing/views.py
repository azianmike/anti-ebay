from django.shortcuts import render
from django.template.defaulttags import csrf_token
import mysql.connector
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'addListing.html',{})
