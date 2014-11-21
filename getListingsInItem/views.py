from django.shortcuts import render
import mysql.connector
# Create your views here.
from django.http import HttpResponse
import json

# Create your views here.
def getListingsInItemJSON(request):
    #return render(request, 'insertListing.html',{})
    itemId = request.POST.get("itemId", "")    
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("getListingsInItem", (itemId,))
    cnx.commit()

    returnArray = []
    for result in cursor.stored_results():
        for item in result.fetchall():
            returnItem = {}
            returnItem['categoryId'] = item[0]
            returnItem['categoryName'] = item[1]
            returnArray.append(returnItem)
    cursor.close()
    return HttpResponse(json.dumps(returnArray))
