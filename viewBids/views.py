from django.shortcuts import render

# Create your views here.
def index(request, listingId=None):
    return render(request, 'viewBids.html',{})
