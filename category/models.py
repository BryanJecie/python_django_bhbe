from django.db import models
from datetime import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=120)
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=120)
    date_created = models.DateTimeField(default=datetime.now())
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand_name
