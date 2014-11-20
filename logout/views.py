from django.shortcuts import render
import mysql.connector
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render(request, 'login.html',{})
    #
    request.session.flush()
    return HttpResponse("You've logged out!")




