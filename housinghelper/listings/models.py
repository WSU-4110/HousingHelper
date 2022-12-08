from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.



class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.IntegerField()
    image=models.ImageField(null=True,blank=True, upload_to="images/")
    option=(('Selling', 'Selling'),('Renting', 'Renting'))
    choice= models.CharField(max_length=10,choices=option,null=True,blank=True)
    housing_option=(('House', 'House'),('Apartment', 'Apartment'),('Condo', 'Condo'),('Townhouse', 'Townhouse'))
    housing_type= models.CharField(max_length=10,choices=housing_option,null=True,blank=True)
    favorite = models.ManyToManyField(User, related_name='favorites', default=None, blank = True)

    def __str__(self):
        return self.title
