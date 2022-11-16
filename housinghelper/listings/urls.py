from django.urls import path
from . import views

from .views import deletelisting

from django.conf import settings
from .views import SearchResultsView, HomePageView

urlpatterns = [
    path('', views.index, name='index'),
    #path('listings', views.listings, name='listings'),
    path('listing/<int:pk>/', views.listing, name='listing'),
    path('createlisting/', views.createlisting, name='createlisting'),
    path('updatelisting<int:pk>/', views.updatelisting, name='updatelisting'),
    path('listing/<pk>/delete/', deletelisting),
    path('calcmortgage/', views.calcmortgage, name='calcmortgage'),
    path('browselisting/', views.browselisting, name='browselisting'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(), name='home'),

]
