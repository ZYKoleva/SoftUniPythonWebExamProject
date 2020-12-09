from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

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


class TypePremise(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NumberRooms(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SaleOrRent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Construction(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Furniture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Elevator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SortOptions(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ad(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    comments_reject = models.TextField(blank=True)
    phone_number = models.CharField(max_length=14)
    date_modified = models.DateField(default=datetime.now())
    sale_or_rent = models.ForeignKey(SaleOrRent, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(DistrictCity, on_delete=models.CASCADE)
    area = models.ForeignKey(DistrictCityArea, on_delete=models.CASCADE)
    type_premise = models.ForeignKey(TypePremise, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    square_meters = models.PositiveIntegerField()
    floor = models.IntegerField()
    total_floors = models.IntegerField()
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    number_rooms = models.ForeignKey(NumberRooms, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    built_date = models.CharField(max_length=4, blank=True)
    description = models.TextField()
    counter_seen = models.IntegerField(default=0)

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

    def __str__(self):
        return f'{self.id}:  {self.city} {self.area} {self.type_premise}'

    def increase_counter_seen(self):
        self.counter_seen += 1
        return self.counter_seen


class AdditionalFilter(models.Model):
    pending_approval = models.BooleanField(default=False)
    my_add = models.BooleanField(default=False)
    type_premise = models.ForeignKey(TypePremise, on_delete=models.CASCADE, blank=True)
    number_rooms = models.ForeignKey(NumberRooms, on_delete=models.CASCADE, blank=True)
    sort = models.ForeignKey(SortOptions, on_delete=models.CASCADE, blank=True)
    sale_or_rent = models.ForeignKey(SaleOrRent, on_delete=models.CASCADE, blank=True)
