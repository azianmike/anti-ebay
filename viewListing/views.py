from django.shortcuts import render
#from django.shortcuts import render_to
# Create your views here.
from django.template.defaulttags import csrf_token
import mysql.connector
from django.http import HttpResponse

# Create your views here.
#@render('viewListing.html',{})
def index(request, listingId=None):
    return render(request, 'viewListing.html',{})
    #return HttpResponse("Hello, world. You're at the view listing index.")

def viewListingPost(request):
    listingID = request.POST.get("listingID","")
    cnx = mysql.connector.connect(user='root',database='antiebay')
    cursor = cnx.cursor()
    #errorMsg = ''render(request, 'viewListing.html',{})
    ret = cursor.callproc("getListing", (listingID,))
    cnx.commit()
    responseString = '<p>test</p>'
    responseString += '<br>'
    
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
#    responseString += str(cursor.stored_results().fetchone()) 
    cursor.close()
    args = {}
    args["username"] = username
    args["description"] = description  
    args["maxPrice"] = maxPrice
    args["itemName"] = itemName
    args["category"] = category
    args["itemName"] = itemName
    args["itemDescription"] = itemDescription
    args["condition"] = condition
    args["listingID"] = listingID
    return render(request, 'viewListingPost.html',args)




