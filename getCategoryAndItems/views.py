from django.shortcuts import render
import mysql.connector
# Create your views here.
from django.http import HttpResponse
import json

# Create your views here.
def getCategories(request):
    #return render(request, 'insertListing.html',{})
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("getCategories", ())
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

def getItems(request):
    categoryId = request.POST.get("categoryId", "")
    
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("getItems", (categoryId,))
    cnx.commit()

    returnArray = []
    for result in cursor.stored_results():
        for item in result.fetchall():
            returnItem = {}
            returnItem['itemId'] = item[0]
            returnItem['itemName'] = item[1]
            returnArray.append(returnItem)
    return HttpResponse(json.dumps(returnArray))
