from django.shortcuts import render
from django.template.defaulttags import csrf_token
# Create your views here.
import mysql.connector
from django.http import HttpResponse

# Create your views here.
def index(request):
    listingID = request.POST.get("listingID", "")
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''render(request, 'viewListing.html',{})
    ret = cursor.callproc("deleteListing", (listingID,(0, 'CHAR')))
    cnx.commit()    
    returnResponse = '<p>'+str(ret[-1]) + ' deleting the listing number '+str(listingID)+'</p>'
    return HttpResponse(returnResponse)    
