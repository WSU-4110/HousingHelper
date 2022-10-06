from django.urls import path
from . import views

from .views import deletelisting

from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    #path('listings', views.listings, name='listings'),
    path('listing/<int:pk>/', views.listing, name='listing-detail'),
    path('createlisting/', views.createlisting, name='createlisting'),
    path('listing/<pk>/delete/', deletelisting),
    path('calcmortgage/', views.calcmortgage, name='calcmortgage'),
    path('browselisting/', views.browselisting, name='browselisting'),
]
