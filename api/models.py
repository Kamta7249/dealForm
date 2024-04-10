from django.db import models

# Create your models here.

class Deal(models.Model):
    dealsOwner = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)
    customerName = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    dealTitle = models.CharField(max_length=200)
    expectedRevenue = models.FloatField()
    expectedDate = models.CharField(max_length=100)