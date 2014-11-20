from django.shortcuts import render
import mysql.connector
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'login.html',{})
    #return HttpResponse("Hello, world. You're at the login index.")

def loginPost(request):
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''
    ret = cursor.callproc("login", (email,password,(0,'CHAR')))
    cnx.commit()
    cursor.close()
    responseString = '';    
    if ret[-1] == 'Success':
        responseString += '<p>Logged in as: '+ email + '</p>'    
    else:    
        responseString += '<p> Login ' + str(ret[-1]) + '</p>'
    return HttpResponse(responseString)
