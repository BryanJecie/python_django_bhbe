from django.db import models

# from .models import Supplier


# def get_code():
#     count = models.objects.count()
#     return count


class Supplier(models.Model):

    # count = models.all()

    supplier_code = models.CharField(max_length=20)
    supplier_name = models.CharField(max_length=25)
    supplier_email = models.EmailField(max_length=254)
    supplier_phone = models.CharField(max_length=200)
    supplier_address = models.TextField()
    supplier_status = models.CharField(max_length=10, default="active")

    def __str__():
        return self

    # def get_supplier(id):
    #     return self.Supplier.find(id)

    # def get_suppliers():
    #     return self.Supplier.object.all()
