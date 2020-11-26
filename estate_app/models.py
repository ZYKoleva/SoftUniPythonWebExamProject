from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from static.others.filter_choice import SALE_RENT_CHOICES, DISTRICT_CHOICES, CITY_CHOICES, AREA_CHOICES, TYPE_CHOICES, \
    CONSTRUCTION_CHOICES, ROOM_CHOICES, FURNITURE_CHOICES, ELEVATOR_CHOICES, SEARCH_TYPE_CHOICES, SEARCH_ROOM_CHOICES, \
    SEARCH_SORT_CHOICES, SEARCH_SALE_RENT_CHOICES


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DistrictCity(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DistrictCityArea(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(DistrictCity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ad(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_modified = models.DateField(default=datetime.now())
    sale_or_rent = models.CharField(max_length=100, choices=SALE_RENT_CHOICES, blank=False)
    district = models.CharField(max_length=100, choices=DISTRICT_CHOICES, blank=False)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, blank=False)
    area = models.CharField(max_length=100, choices=AREA_CHOICES, blank=False)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, blank=False)
    price = models.IntegerField()
    floor = models.IntegerField()
    total_floors = models.IntegerField()
    construction = models.CharField(max_length=100, choices=CONSTRUCTION_CHOICES, blank=False)
    image_one = models.ImageField(upload_to='images', blank=True)
    image_two = models.ImageField(upload_to='images', blank=True)
    image_three = models.ImageField(upload_to='images', blank=True)
    image_four = models.ImageField(upload_to='images', blank=True)
    image_five = models.ImageField(upload_to='images', blank=True)
    image_six = models.ImageField(upload_to='images', blank=True)
    image_seven = models.ImageField(upload_to='images', blank=True)
    image_eight = models.ImageField(upload_to='images', blank=True)
    image_nine = models.ImageField(upload_to='images', blank=True)
    image_ten = models.ImageField(upload_to='images', blank=True)
    number_rooms = models.CharField(max_length=100, choices=ROOM_CHOICES, blank=False)
    furniture = models.CharField(max_length=100, choices=FURNITURE_CHOICES, blank=False)
    elevator = models.CharField(max_length=100, choices=ELEVATOR_CHOICES, default='Не')
    built_date = models.CharField(max_length=4, blank=True)
    description = models.TextField()
    top_offer = models.BooleanField(default=False)
    counter_seen = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}:  {self.city} {self.area} {self.type}'

    def increase_counter_seen(self):
        self.counter_seen += 1
        return self.counter_seen


class AdditionalFilter(models.Model):
    type = models.CharField(max_length=100, choices=SEARCH_TYPE_CHOICES, default=SEARCH_TYPE_CHOICES[0])
    number_rooms = models.CharField(max_length=100, choices=SEARCH_ROOM_CHOICES, default = SEARCH_ROOM_CHOICES[0])
    sort = models.CharField(max_length=100, choices=SEARCH_SORT_CHOICES, default=SEARCH_SORT_CHOICES[0])
    sale_or_rent = models.CharField(max_length=100, choices=SEARCH_SALE_RENT_CHOICES, default=SEARCH_SALE_RENT_CHOICES[0])


class LookingFor(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_modified = models.DateField(default=datetime.now())
    title = models.CharField(max_length=100)
    description = models.TextField()
    approved = models.BooleanField(default=False)