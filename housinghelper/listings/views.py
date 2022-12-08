from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from django.http import HttpResponse
from .models import Listing
from .forms import ListingForm, TestForm, CreateUserForm
from django.shortcuts import render, redirect
from .filters import ListingFilter
from .filters import ListingFilter

from django.views.generic import ListView, TemplateView
from django.db.models import Q # new
from django.contrib.auth.models import User



@user_passes_test(lambda u: u.is_superuser)
@login_required
def createuser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/createuser.html', context)

def listusers(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'listings/listusers.html', context)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is created for ' + user)
                return redirect('login')
                            
        context = {'form':form}
        return render(request, 'listings/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'listings/login.html', context)

def logoutUser(request):
        logout(request)
        return redirect('login')



# def loginPage(request):
#     return render(request, 'listings/login_register.html')



def home(request):
    return render(request, 'home.html')




def index(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        'listing_filter' : listing_filter
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
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/listing_form.html', context)
    
def browselisting(request):
    
    all_listings=Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=all_listings)
    context = {
        'listing_filter' : listing_filter
    }
    return render(request, 'listings/browse_houses.html', context)
 
def rentlisting(request):
    
    rent_listings=Listing.objects.all()


    rent_listings = rent_listings.filter(choice='Renting')

    listing_filter = ListingFilter(request.GET, queryset=rent_listings)
    context = {
        'listing_filter' : listing_filter
    }
    return render(request, 'listings/renting_houses.html', context)
   
def selllisting(request):
    
    sell_listings=Listing.objects.all()


    sell_listings = sell_listings.filter(choice='Selling')

    listing_filter = ListingFilter(request.GET, queryset=sell_listings)
    context = {
        'listing_filter' : listing_filter
    }
    return render(request, 'listings/selling_houses.html', context)


def deletelisting(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')


def updatelisting(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance = listing)
    if request.method == 'POST':
        form = ListingForm(request.POST,request.FILES, instance = listing)
        if form.is_valid():
            form.save()
            return redirect('/browselisting')
    context = {'form': form}
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
    template_name = 'search_listing.html'


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


#favorites comes after user authentication
@ login_required
def favoriteHouse(request, pk):
    Listing = get_object_or_404(Listing, pk=pk)
    if Listing.favorite.filter(pk=request.user.pk).exists():
        Listing.favorite.remove(request.user)
    else:
        Listing.favorite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@ login_required
def favoriteList(request):
    favList=Listing.objects.all()


    favList = favList.filter(favorite=True)

    listing_filter = ListingFilter(request.GET, queryset=favList)
    context = {
        'listing_filter' : listing_filter
    }

    return render(request, 'listings/favorites.html', context)



def houseamount(request):
    
    allobj=Listing.objects.all()

    if request.method == 'POST':
        totalCost=request.POST.get('Total_cost_over_term')

        
        
        totalCost=float(totalCost)
        allobj = allobj.filter(price__lte=totalCost)
    
    allobj=allobj.filter(choice='Selling')
    listing_filter = ListingFilter(request.GET, queryset=allobj)
    context = {
        'listing_filter' : listing_filter
    }
    return render(request, 'listings/calc_result.html', context)
 
   