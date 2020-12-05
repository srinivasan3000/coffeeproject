from django.db import models

# Create your models here.

class Reviews(models.Model):
    review=models.TextField()

class Order(models.Model):
    address=models.TextField()
    food = models.CharField(max_length=250)
    number=models.IntegerField()
