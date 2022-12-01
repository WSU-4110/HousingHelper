from django.test import TestCase
from django.test import SimpleTestCase
from django.http import HttpResponse
from django.urls import reverse, resolve
from listings.views import calcmortgage, favorite ,HomePageView, deletelisting
from listings.filters import ListingFilter
from listings.models import Listing

class TestUrls(TestCase):

    def test_calculateMort(self):
        url = reverse('calcmortgage')
        self.assertEquals(resolve(url).func, calcmortgage)
        print("Calc Site Test")
        print(resolve(url))

    def test_page_delete(self):
        page = self.client.get("self")
        page = self.client.get("/listing/1/delete")
        self.assertTrue(page.status_code, 404)
        print("Deleter Site Test")


    def test_page_main(self):
        page = self.client.get("/home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "main.html")
        print("Main Test")

    def test_page_nav(self):
        page = self.client.get("/home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "navbar.html")
        print("Nav Test")

    def test_updatelisting(self):
        houseListing = Listing.objects.create(
            title = 'housecool',
            description = 'nice',
            price = 10,
            bedrooms = 3,
            bathrooms = 3,
            garage = 3,
            sqft = 10000,
            lot_size = 500,
            image = 'NA.jpg',
            choice = 'Selling'
            )

        houseListing = Listing.objects.create(
            title = 'housecool',
            description = 'nice',
            price = 120000,
            bedrooms = 4,
            bathrooms = 3,
            garage = 3,
            sqft = 10000,
            lot_size = 500,
            image = 'NA.jpg',
            choice = 'Selling'
        )
        self.assertEqual(houseListing.price, 120000)
        print("UpdateHouse Functionality Test")

    def test_filtering(self):
        houseListing2 = Listing.objects.create(
            title = 'housecool',
            description = 'nice',
            price = 10000000,
            bedrooms = 3,
            bathrooms = 3,
            garage = 3,
            sqft = 10000,
            lot_size = 500,
            image = 'NA.jpg',
            choice = 'Selling'
            )

        houseListing = Listing.objects.create(
            title = 'housecool',
            description = 'nice',
            price = 120,
            bedrooms = 4,
            bathrooms = 3,
            garage = 3,
            sqft = 10000,
            lot_size = 500,
            image = 'NA.jpg',
            choice = 'Selling'
        )
        listings = Listing.objects.all()
        listing_filter = Listing.objects.filter(
            price = 200,
            bedrooms = 2,
            bathrooms = 1,
           
        )
        #listing_filter = ListingFilter(), queryset=listings)
        self.assertTrue(houseListing, listing_filter)
        print("Filtering Functionality Test")

