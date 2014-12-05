from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the register index.")
    #form = ContactForm(request.POST)
    return render(request, 'searchListings.html',{})
