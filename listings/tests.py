from django.test import TestCase
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Listing
from .forms import ListingForm, TestForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.db.models import Q # new

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from listings.views import home, index, listing,SearchResultsView,HomePageView, createlisting, rentlisting, updatelisting, deletelisting, browselisting, selllisting, houseamount, favoriteHouse, favoriteList, calcmortgage, createuser, listusers



class TestViews(TestCase):
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "listings/index.html")

    def test_get_listing_page(self):
        page = self.client.get("/listing/1")
        self.assertEqual(page.status_code, 301)

    def test_get_search_page(self):
        page = self.client.get("/home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search_listing.html")


    def test_listing_model(self):
        listing = Listing.objects.create(
            title = 'test title',
            description = 'test description',
            price = 100,
            bedrooms = 2,
            bathrooms = 1,
            garage = 1,
            sqft = 1000,
            lot_size = 1000,
            image = 'test.jpg',
            choice = 'test choice',
        )
        self.assertEqual(str(listing), 'test title')

    def test_listing_form(self):
        form = ListingForm({
            'title': 'test title',
            'description': 'test description',
            'price': 100,
            'bedrooms': 2,
            'bathrooms': 1,
            'garage': 1,
            'sqft': 1000,
            'lot_size': 1000,
            'image': 'test.jpg',
            'choice': 'Selling',
        })
        self.assertTrue(form.is_valid())

    def test_listing_form_no_data(self):
        form = ListingForm({})
        self.assertFalse(form.is_valid())





class TestUrls(SimpleTestCase):
    def test_index(self):
        url = reverse('index')
        
        self.assertEquals(resolve(url).func, index)
        
    
   
    def test_createlisting(self):
        url = reverse('createlisting')
        self.assertEquals(resolve(url).func, createlisting)
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)

    def test_updatelisting(self):
        url = reverse('updatelisting', args=['1'])
        self.assertEquals(resolve(url).func, updatelisting)
        
   
    def test_browselisting(self):
        url = reverse('browselisting')
        self.assertEquals(resolve(url).func, browselisting)
        
    

    def test_listing(self):
        url = reverse('listing-detail', args=['1'])
        self.assertEquals(resolve(url).func, listing)
       

   
    def test_search_results(self):
        url = reverse('search_results')
        self.assertEquals(resolve(url).func.view_class, SearchResultsView)
        

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePageView)
        

    def test_deletelisting(self):
        url = reverse('deletelisting', args=['1'])
        self.assertEquals(resolve(url).func, deletelisting)
        



    def test_rentlisting(self):
        url = reverse('rentlisting')
        self.assertEquals(resolve(url).func, rentlisting)
        
    def test_selllisting(self):
        url = reverse('selllisting')
        self.assertEquals(resolve(url).func, selllisting)

    def test_houseamount(self):
        url = reverse('houseamount')
        self.assertEquals(resolve(url).func, houseamount)

    def test_favoritelist(self):
        url = reverse('favoriteList')
        self.assertEquals(resolve(url).func, favoriteList)

    def test_createuser(self):
        url = reverse('createuser')
        self.assertEquals(resolve(url).func, createuser)

    def test_listusers(self):
        url = reverse('listusers')
        self.assertEquals(resolve(url).func, listusers)

    def test_calcmortgage(self):
        url = reverse('calcmortgage')
        self.assertEquals(resolve(url).func, calcmortgage)

        

    
