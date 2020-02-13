from django.contrib import admin
from products.models import Product, Barcode, Product_StockIn, StockIn_Summary

admin.site.register(Product)
admin.site.register(Barcode)
admin.site.register(Product_StockIn)
admin.site.register(StockIn_Summary)