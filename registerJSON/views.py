from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import mysql.connector
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    #return render(request, 'login.html',{})
    returnDict = {}
    returnDict['success'] = -1
    #start POST and db stuff
    email = request.POST.get("email", "")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    address = request.POST.get("address","")
    firstName = request.POST.get("firstName","")
    lastName = request.POST.get("lastName","")
    
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''
    ret = cursor.callproc("registerNewUser", (username,email,password,address,firstName,lastName,(0,'CHAR')))
    cnx.commit()
    cursor.close()
    
    if ret[-1] == 'User Added':
        returnDict['success'] = 1
        request.session['has_loggedin'] = True
        request.session['username'] = username
        request.session.modified = True
    elif ret[-1] == 'Username and email already being used.':
        returnDict['success'] = -3
    elif ret[-1] == 'Username already being used.':
        returnDict['success'] = -1
    elif ret[-1] == 'Email already being used.':
        returnDict['success']= -2
    return HttpResponse(json.dumps(returnDict))


