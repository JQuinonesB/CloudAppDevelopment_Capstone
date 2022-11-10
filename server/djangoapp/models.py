from django.db import models
from django.utils.timezone import now
from django.core import serializers
import uuid
import json


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    maker_name = models.CharField(null=False, max_length=30, default='BMW')
    description = models.CharField(null=False, max_length=500)

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.maker_name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):

    SUV = 'SUV'
    SEDAN = 'Sedan'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    TYPE_CHOICES = [
        (SUV, 'SUV'),
        (SEDAN, 'Sedan'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe')]

    model_name = models.CharField(null=False, max_length=30, default='X7')
    dealerID = models.IntegerField(default=1,primary_key=True)
    car_type = models.CharField(null=False,max_length=30, choices=TYPE_CHOICES, default=SEDAN)
    year = models.DateField(null=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)


    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.model_name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, id, review, purchase_date, car_make, car_model, car_year, sentiment):
        # Review dealership
        self.dealership = dealership
        # review name
        self.name = name
        # customer purchase
        self.purchase = purchase
        # review id
        self.id = id
        # review
        self.review = review
        # purchase date reviewer
        self.purchase_date = purchase_date
        # review car maker
        self.car_make = car_make
        # review car model
        self.car_model = car_model
        # review car year
        self.car_year = car_year
        # review sentiment
        self.sentiment = sentiment

    def __str__(self):
        return "Review: " + self.review