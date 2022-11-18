
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from listings.views import home, index, listing,SearchResultsView,HomePageView, createlisting, updatelisting, deletelisting, browselisting





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

    
   
    


    