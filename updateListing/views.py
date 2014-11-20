from django.shortcuts import render
from django.template.defaulttags import csrf_token
# Create your views here.
import mysql.connector
from django.http import HttpResponse

# Create your views here.
def index(request):
    listingID = request.POST.get("listingID", "")    
    #return HttpResponse("Hello, world. You're at the update listing index." + str(listingID))
    args = {}
    args["listingID"]=listingID
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''render(request, 'viewListing.html',{})
    ret = cursor.callproc("getListing", (listingID,))
    cnx.commit()

    listingResult = ''
    for result in cursor.stored_results():
        listingResult = result.fetchone()

    listingID = listingResult[0]
    username = listingResult[1]
    description = listingResult[2]
    maxPrice = listingResult[3]
    itemID = listingResult[4]
    itemName = listingResult[5]
    itemDescription = listingResult[6]
    itemPictureUrl = listingResult[7]
    category = listingResult[8]
    condition = listingResult[9]

    args = {}
    args["listingID"]=listingID    
    args["description"] = description
    args["maxPrice"] = maxPrice
    args["newChecked"] = ''
    args["used1Checked"] = ''
    args["used2Checked"] = ''
    args["used3Checked"] = ''
    args["brokenChecked"] = ''
    if condition == 'New - In Box':
        args["newChecked"] = 'checked'
    if condition == 'Used - Like New':
        args["used1Checked"] = 'checked'
    if condition == 'Used - Moderate':
        args["used2Checked"] = 'checked'
    if condition == 'Used - Poor':
        args["used3Checked"] = 'checked'
    if condition == 'Broken':
        args["brokenChecked"] = 'checked'
    return render(request, 'updateListing.html',args)

def updateListingPost(request):
    listingID = request.POST.get("listingID", "")
    description = request.POST.get("description","")
    maxPrice = request.POST.get("maxPrice","")
    condition = request.POST.get("condition","")    

    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    ret = cursor.callproc("updateListing", (listingID,description,maxPrice,condition,(0,'CHAR')))
    cnx.commit()
    returnResponse = '<p>'+str(ret[-1]) + ' updating the listing </p>'
    return HttpResponse(returnResponse)

