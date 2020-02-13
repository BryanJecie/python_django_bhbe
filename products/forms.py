from django.forms import ModelForm
from .models import Product, Barcode, Brand, Product_StockIn, StockIn_Summary



class ProductForm(ModelForm):
   class Meta:
      model = Product
      fields = [
         'brand',
         'product_name',
         'product_subname',
         'product_description',
      ]

class BarcodeForm(ModelForm):
   class Meta:
      model = Barcode
      fields = ['barcode']        