
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import mysql.connector
#from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    #return render(request, 'login.html',{})
    returnDict = {}
   # if request.session.get('has_loggedin',False):
    #    username = request.session.get('username',False)
    #    returnDict['success'] = -2
    #    return HttpResponse(json.dumps(returnDict))

    #start POST and db stuff
    itemId = request.POST.get("itemId", "5")
    listingConditionId = request.POST.get("listingConditionId", "3")
    price = request.POST.get("price", "375")

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("calculateSellProbability", (itemId, listingConditionId, price))
    for result in cursor.stored_results():
        for item in result.fetchall():
            returnDict['probability'] = float(item[0]) * 100
    cnx.commit()
    cursor.close()
    return HttpResponse(json.dumps(returnDict))


