from django.shortcuts import render
#from django.shortcuts import render_to
# Create your views here.
from django.template.defaulttags import csrf_token
import mysql.connector
from django.http import HttpResponse
import json

# Create your views here.
#@render('viewListing.html',{})
    #return HttpResponse("Hello, world. You're at the view listing index.")

def viewListingJSON(request):
    #listingID = request.POST.get("listingID","")
    listingId = request.POST.get('listingId', '')
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''render(request, 'viewListing.html',{})
    ret = cursor.callproc("getListing", (listingId,))
    cnx.commit()
    returnDict={}    
    listingResult = ''
    for result in cursor.stored_results():
        listingResult = result.fetchone()
    
        returnDict['listingId'] = listingResult[0]
        returnDict['username'] = listingResult[1]
        returnDict['description'] = listingResult[2]
        returnDict['maxPrice'] = float(listingResult[3])
        returnDict['itemId'] = listingResult[4]
        returnDict['itemName'] = listingResult[5]
        returnDict['itemDescription'] = listingResult[6]
        returnDict['itemPictureUrl'] = listingResult[7]
        returnDict['category'] = listingResult[8]
        returnDict['condition'] = listingResult[9]
    cursor.close()
    return HttpResponse(json.dumps(returnDict))

def viewMyListingJSON(request):
    #listingID = request.POST.get("listingID","")
    #listingId = request.POST.get('listingId', '')
    if request.session.get('has_loggedin',False):
        username = request.session.get('username',False)
    if username == False:
        returnDict = {}
        returnDict['failure'] = -1
        return HttpResponse(json.dumps(returnDict))
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''render(request, 'viewListing.html',{})
    ret = cursor.callproc("getMyListings", (username,))
    cnx.commit()
    returnDict={}
    returnArray = []
    for result in cursor.stored_results():
        for item in result.fetchall():
            returnItem = {}
            returnItem['listingId'] = item[0]
            returnItem['itemId'] = item[1]
            returnItem['username'] = item[2]
            returnItem['listingDescription'] = item[3]
            returnItem['maxPrice'] = float(item[4])
            returnItem['listingConditionId'] = item[5]
            returnArray.append(returnItem)
    cursor.close()
    return HttpResponse(json.dumps(returnArray))



