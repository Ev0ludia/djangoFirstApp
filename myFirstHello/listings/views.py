from typing import List
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 
                    'listings/hello.html', 
                    {'bands' : bands}
                )

def about(request):
    return HttpResponse('About-us')    
    
def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Listings</h1>
        <p>Listing</p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
        </ul>
    """)  

def contact(request):
    return HttpResponse('Contact us')    