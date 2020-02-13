from django.db import models
from category.models import Brand


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_subname = models.CharField(max_length=120)
    product_description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Barcode(models.Model):
    barcode = models.CharField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.barcode


class Product_StockIn(models.Model):
    prod_stock_no = models.CharField(max_length=100)
    prod_stock_qty = models.FloatField(max_length=11)
    prod_stock_type = models.CharField(max_length=120)
    barcode = models.ForeignKey(Barcode, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.prod_stock_no


class StockIn_Summary(models.Model):
    stock_sum_qty = models.FloatField(max_length=11)
    stock_sum_buying_price = models.FloatField(max_length=120)
    stock_sum_selling_price = models.FloatField(max_length=120)
    stock_sum_status = models.CharField(max_length=120, default='in stock')
    stock_sum_selling_type = models.CharField(max_length=120)
    barcode = models.ForeignKey(Barcode, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.stock_sum_status
