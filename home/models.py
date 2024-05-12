from django.db import models

# Create your models here.

class Post(models.Model):
    CarCompanyName=models.CharField(max_length=250)
    fueltype =models.CharField(max_length=250)
    highwaympg=models.CharField(max_length=100)
    citympg=models.CharField(max_length=100)
    horsepower=models.CharField(max_length=100)
    curbweight=models.CharField(max_length=100)

    def __str__(self):
        return self