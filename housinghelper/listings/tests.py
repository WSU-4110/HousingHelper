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
from listings.views import home, index, listing,SearchResultsView,HomePageView, createlisting, updatelisting, deletelisting, browselisting



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
        print(resolve(url))
    
   
    def test_createlisting(self):
        url = reverse('createlisting')
        self.assertEquals(resolve(url).func, createlisting)
        response = self.client.get(url)
        print("testing createlisting url...")
        print(resolve(url))
        self.assertEquals(response.status_code, 200)

    def test_updatelisting(self):
        url = reverse('updatelisting', args=['1'])
        self.assertEquals(resolve(url).func, updatelisting)
        print("testing updatelisting url...")
        print(resolve(url))
   
    def test_browselisting(self):
        url = reverse('browselisting')
        self.assertEquals(resolve(url).func, browselisting)
        print("testing browselisting url...")
        print(resolve(url))
    

    def test_listing(self):
        url = reverse('listing', args=['1'])
        self.assertEquals(resolve(url).func, listing)
        print("testing listing url...")
        print(resolve(url))

   
    def test_search_results(self):
        url = reverse('search_results')
        self.assertEquals(resolve(url).func.view_class, SearchResultsView)
        print("testing search_results url...")
        print(resolve(url))

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePageView)
        print("testing home url...")
        print(resolve(url))

    
   
    
