from django.shortcuts import render
import mysql.connector
# Create your views here.
from django.http import HttpResponse
from decimal import Decimal
import json

# Create your views here.
def bidJSON(request):
    #return render(request, 'insertListing.html',{})
    username = request.session.get('username',False)
    if username == False:
        return HttpResponse("not logged in")
    price = request.POST.get("price", "")
    itemId = request.POST.get("itemId", "")
    listingId = request.POST.get("listingId", "")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("addBid", (username,itemId,listingId,price))
    cnx.commit()

    cursor.close()
    returnDict = {}
    returnDict['success'] = 1
    return HttpResponse(json.dumps(returnDict))

def getBidsJSON(request):
    #return render(request, 'insertListing.html',{})
    listingId = request.POST.get("listingId", "")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("getBids", (listingId,))
    cnx.commit()

    returnArray = []
    for result in cursor.stored_results():
        for item in result.fetchall():
            returnItem = {}
            returnItem['bidId'] = item[0]
            returnItem['price'] = float(item[1])
            returnItem['username'] = item[2]
            returnItem['listingId'] = item[3]
            returnItem['itemId'] = float(item[4])
            returnArray.append(returnItem)
    cursor.close()
    return HttpResponse(json.dumps(returnArray))
