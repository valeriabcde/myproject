from django.db import models

# Create your models here.

class Feedback(models.Model):
    email = models.CharField(max_length=255)
    text = models.TextField()

class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=20)
    price = models.IntegerField()
