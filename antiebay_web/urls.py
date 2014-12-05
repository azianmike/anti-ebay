from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'antiebay_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index', name='home',),
    url(r'^login/', 'login.views.index'),
    url(r'^loginPost/', 'login.views.loginPost'),
    url(r'^register/', 'register.views.index'),
    url(r'^addListing/', 'addListing.views.index'),
    url(r'^insertListingPost/', 'insertListing.views.insertListingPost'),
    url(r'^viewListing/$', 'viewListing.views.index'),
    url(r'^viewListingPost/', 'viewListing.views.viewListingPost'),
    url(r'^updateListing/', 'updateListing.views.index'),    
    url(r'^updateListingPost/', 'updateListing.views.updateListingPost'),
    url(r'^registerPost/', 'register.views.registerPost'),
    url(r'^deleteListing/', 'deleteListing.views.index'),
    url(r'^loginJSON/', 'loginJSON.views.index'),
    url(r'^checkLoginJSON/', 'loginJSON.views.checkIfLoggedIn'),
    url(r'^registerJSON/', 'registerJSON.views.index'),
    url(r'^logout/', 'logout.views.index'),    
    url(r'^getCategoriesJSON/', 'getCategoryAndItems.views.getCategories'),
    url(r'^getItemsJSON/', 'getCategoryAndItems.views.getItems'),    
    url(r'^addListingJSON/', 'addListingJSON.views.addListingJSON'),
    url(r'^getListingsInItemJSON/', 'getListingsInItem.views.getListingsInItemJSON'),
    url(r'^bidJSON/', 'bidJSON.views.bidJSON'),
    url(r'^getBidsJSON/', 'bidJSON.views.getBidsJSON'),
    url(r'^searchListings/', 'searchListings.views.index'),
    url(r'^viewListingNew/', 'viewListingNew.views.index'),
    url(r'^getListingJSON/$', 'viewListingJSON.views.viewListingJSON'),
    url(r'^getMyListingsJSON/$', 'viewListingJSON.views.viewMyListingJSON'),
    url(r'^finishListingJSON/$', 'finishListingJSON.views.finishListingJSON'),
    url(r'^calculateSellProbabilityJSON/$', 'calculateSellProbabilityJSON.views.index'),
)
