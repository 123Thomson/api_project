from django.db import models


# Create your models here.
class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=100)
    ram_size = models.IntegerField()
    storage_size = models.IntegerField()
    storage_type = models.CharField(max_length=50)
    display_size = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='laptop_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.brand} {self.model} - {self.processor_type}"
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
