from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import Form, ModelForm

import uuid

from constants import Constants

# class Location(models.Model):
#     latlong = models.CharField(max_length=200, primary_key=True)
#     latitude = models.CharField(max_length=100)
#     longitude = models.CharField(max_length=100)
#     street = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#
#
# class User(models.Model):
#     user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user_first_name = models.CharField(max_length=40)
#     user_last_name = models.CharField(max_length=40)
#     user_email = models.EmailField()
#     is_cook = models.BooleanField
#     latitude = models.CharField(max_length=100)
#     longitude = models.CharField(max_length=100)
#     latlong = models.ForeignKey(Location, on_delete=models.CASCADE)
#
#
# class Food(models.Model):
#     food_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     food_name = models.CharField(max_length=50)
#     food_cost = models.DecimalField(max_digits=5, decimal_places=2)
#     food_quantity = models.FloatField()
#     food_units = models.CharField(max_length=10)
#     food_description = models.CharField(max_length=1000)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Order(models.Model):
#     order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     order_date_time = models.DateTimeField(format(Constants.DATE_TIME_FORMAT))
#     order_total = models.DecimalField(max_digits=8, decimal_places=2)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
# class Payment(models.Model):
#     payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


# class Schedule(models.Model):
#     interview_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     interviewDate = models.DateTimeField(Constants.DATE_FORMAT)
#     interviewTime = models.DateTimeField(Constants.TIME_FORMAT)
#     email = models.EmailField()


########### forms #############
# class AddUserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ["user_first_name", "user_last_name", "user_email"]
#
#
# class AddFoodProductForm(ModelForm):
#     class Meta:
#         model = Food
#         fields = ["food_name", "food_cost", "food_quantity", "food_units",
#                   "food_description"]
#
# class AddLocation(ModelForm):
#     class Meta:
#         model = Location
#         fields = ["latlong", "latitude", "longitude", "street", "city", "state", "country"]

class Appointments(models.Model):
    interview_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interview_date = models.DateTimeField(format(Constants.DATE_TIME_FORMAT))
    interview_time = models.DateTimeField(Constants.TIME_FORMAT)
    email = models.EmailField()

class SchedulerForm(Form):
    scheduleDate = forms.CharField()
    scheduleTime = forms.CharField()
    scheduleTopic = forms.CharField()
    email = forms.EmailField()