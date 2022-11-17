import django_filters

from .models import Listing

class ListingFilter(django_filters.FilterSet):
 
    class Meta:
        model = Listing
        fields = {'price' : ['lte'], 
        'bedrooms' : ['gte'],
        'bathrooms' : ['gte'],
        'garage' : ['gte']}

        