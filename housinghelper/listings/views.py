from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Listing
from .forms import ListingForm
from django.shortcuts import render, redirect

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/index.html', context)


def listing(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def createlisting(request):
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/listing_form.html', context)
    context = {
        'form': form
            }
    return render(request, 'listings/listing_form.html', context)

def updatelisting(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance = listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/updatelisting.html', context)
    context = {
        'form': form
            }
    return render(request, 'listings/updatelisting.html', context)
