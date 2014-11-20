from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.defaulttags import csrf_token
import mysql.connector
# Create your views here.
from django.http import HttpResponse

# Create your views here.
#{% csrf_token %}
#@csrf_token
def index(request):
    #return HttpResponse("Hello, world. You're at the register index.")
    #form = ContactForm(request.POST)
    return render(request, 'register.html',{})


#{% csrf_token %}
def registerPost(request):
    email = request.POST.get("email", "")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    confirmPassword = request.POST.get("confirmPassword", "")
    address = request.POST.get("address","")
    firstName = request.POST.get("firstName","")
    lastName = request.POST.get("lastName","")
    responseString = '<p>Hello, world. You\'re at the register post index.\n</p>'
    
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''
    ret = cursor.callproc("registerNewUser", (username,email,password,address,firstName,lastName,(0,'CHAR')))
    cnx.commit()
    cursor.close()
    responseString += '<br>'
    responseString += '<br>'
    responseString += '<p>' + str(ret[-1]) + '</p>'
    return HttpResponse(responseString)


