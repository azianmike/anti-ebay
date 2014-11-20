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
    if request.session.get('has_loggedin',False):
        username = request.session.get('username',False)
        returnDict['success'] = -2
        return HttpResponse(json.dumps(returnDict))

    #start POST and db stuff
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("login", (username,password,(0,'CHAR')))
    cnx.commit()
    cursor.close()
    if ret[-1] == 'Success':
        returnDict['success'] = 1
        request.session['has_loggedin'] = True
        request.session['username'] = username
        request.session.modified = True
    return HttpResponse(json.dumps(returnDict))

def checkIfLoggedIn(request):
    returnDict = {}
    returnDict['success'] = 1
    if request.session.get('has_loggedin',False):
        username = request.session.get('username',False)
        returnDict['success'] = username
        return HttpResponse(json.dumps(returnDict))
    else:
        return HttpResponse(json.dumps(returnDict))
