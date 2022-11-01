from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Listing
from .forms import ListingForm, TestForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.db.models import Q # new


def home(request):
    return render(request, 'home.html')

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



# Transforming the createlisting function to use the factory method
def createlisting(request):
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/listing_form.html', context)



# implement the createlisting function using the factory method

def createlisting(request):
    form = ListingForm()

    valid_form(request)
    context = {'form': form}
    return render(request, 'listings/listing_form.html', context)


def valid_form(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
 




def browselisting(request):
    
    all_listings=Listing.objects.all

    return render(request, 'listings/browse_houses.html', {'all':all_listings})
   

def deletelisting(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')



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



class SearchResultsView(ListView):
    model = Listing
    template_name = 'listings/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Listing.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list

class HomePageView(TemplateView):
    template_name = 'home.html'


def calcmortgage(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/calc_form.html', context)
