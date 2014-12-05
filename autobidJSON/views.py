
from django.shortcuts import render
import mysql.connector
# Create your views here.
from django.http import HttpResponse
from decimal import Decimal
import json

# Create your views here.
def autobidJSON(request):
    #return render(request, 'insertListing.html',{})
    username = request.session.get('username','test')
    if username == False:
        return HttpResponse("not logged in")
    price = request.POST.get("price", '100')
    itemId = request.POST.get("itemId", '6')
    listingConditionId = request.POST.get("listingConditionId", "3")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("autoBid", (username,itemId,listingConditionId,price))
    cnx.commit()
    returnDict = {}
    for result in cursor.stored_results():
        for item in result.fetchall():
            returnDict['size']=item[0]
    cursor.close()
    return HttpResponse(json.dumps(returnDict))
