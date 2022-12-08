from django.urls import path
from . import views

from .views import deletelisting

from django.conf import settings
from .views import SearchResultsView, HomePageView

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('', views.index, name='index'),
    #path('listings', views.listings, name='listings'),
    path('listing/<int:pk>/', views.listing, name='listing-detail'),
    path('createlisting/', views.createlisting, name='createlisting'),
    path('updatelisting<int:pk>/', views.updatelisting, name='updatelisting'),
    path('listing/<int:pk>/', views.favoriteHouse, name='favoriteHouse'),
    path('listing/<pk>/delete/', views.deletelisting, name="deletelisting"),
    path('calcmortgage/', views.calcmortgage, name='calcmortgage'),
    path('browselisting/', views.browselisting, name='browselisting'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(), name='home'),
    path('favorites/', views.favoriteList, name='favoriteList'),
    path('createuser/', views.createuser, name='createuser'),
    path('listusers/', views.listusers, name='listusers'),
]
