from django.shortcuts import render
from django.template.defaulttags import csrf_token
import mysql.connector
# Create your views here.
from django.http import HttpResponse
import json
# Create your views here.

def addListing(request):
    #email = request.POST.get("email", "")
    #username = request.POST.get("username", "")
    username = request.session.get('username',False)
    itemID = request.POST.get("itemID", "")
    description = request.POST.get("description", "")
    condition = request.POST.get("condition", "")
    maxPrice = request.POST.get("maxPrice", "")
    responseString = ''
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''
    ret = cursor.callproc("addListing", (username,itemID,description,condition,maxPrice,(0,'CHAR')))
    cnx.commit()
    cursor.close()
    returnDict = {}
    returnDict['success'] = 1
    if ret[-1] == None:
        returnDict['success'] = -1
    return HttpResponse(json.dumps(returnDict))
    #return HttpResponse("hi")


