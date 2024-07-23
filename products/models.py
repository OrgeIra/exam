from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
