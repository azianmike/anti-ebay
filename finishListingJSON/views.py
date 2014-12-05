from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import mysql.connector
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
import json

# Create your views here.
def finishListingJSON(request):
    #return render(request, 'login.html',{})
    returnDict = {}
    #returnDict['success'] = -1
    #if request.session.get('has_loggedin',False):
    #    username = request.session.get('username',False)
    #    returnDict['success'] = -2
    #    return HttpResponse(json.dumps(returnDict))

    #start POST and db stuff
    listingId = request.POST.get("listingId", "62")
    closingPrice = request.POST.get("closingPrice", "350")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("finishListing", (listingId,closingPrice))
    cnx.commit()
    cursor.close()
    returnDict['success'] = 1
    return HttpResponse(json.dumps(returnDict))
