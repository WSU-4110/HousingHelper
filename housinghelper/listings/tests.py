from django.test import TestCase



class TestViews(TestCase):
    def test_get_index_page(self):
        page = self.client.get("/listings/index.html")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "listings/index.html")

    def test_get_listing_page(self):
        page = self.client.get("/listings/listing.html")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "listings/listing.html")

    def test_get_search_results_page(self):
        page = self.client.get("/listings/search_results.html")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "listings/search_results.html")


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
            option = 'test option',
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
            'option': 'test option',
            'choice': 'test choice',
        })
        self.assertTrue(form.is_valid())

    def test_listing_form_no_data(self):
        form = ListingForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['This field is required.'],
            'description': ['This field is required.'],
            'price': ['This field is required.'],
            'bedrooms': ['This field is required.'],
            'bathrooms': ['This field is required.'],
            'garage': ['This field is required.'],
            'sqft': ['This field is required.'],
            'lot_size': ['This field is required.'],
            'image': ['This field is required.'],
            'option': ['This field is required.'],
            'choice': ['This field is required.'],
        })

