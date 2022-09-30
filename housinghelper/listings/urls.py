from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('listings', views.listings, name='listings'),
    path('listing/<int:pk>/', views.listing, name='listing'),
    path('createlisting/', views.createlisting, name='createlisting'),
]
