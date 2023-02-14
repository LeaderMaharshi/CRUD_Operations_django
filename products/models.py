from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)
    price = models.FloatField(null = True)
    image = models.ImageField(upload_to='photos/products')

    def __str__(self):
        return self.name
