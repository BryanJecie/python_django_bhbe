from django.db import models


class Supplier(models.Model):

    supplier_code = models.CharField(max_length=20)
    supplier_name = models.CharField(max_length=25)
    supplier_email = models.EmailField(max_length=254)
    supplier_phone = models.CharField(max_length=200)
    supplier_address = models.TextField()
    supplier_status = models.CharField(max_length=10, default="active")

    def __str__(self):
        return self.supplier_name

