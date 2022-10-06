from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    #path('listings', views.listings, name='listings'),
    path('listing/<int:pk>/', views.listing, name='listing'),
    path('createlisting/', views.createlisting, name='createlisting'),
    path('browselisting/', views.browselisting, name='browselisting'),
]
