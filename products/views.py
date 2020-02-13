import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from utilities.helper import navBar
from .forms import ProductForm, BarcodeForm
from .models import Barcode, Product


def index(request):

   context = {
      "navbar": navBar("products", "manage"),
      'products' : Product.objects.all()
   }

   return render(request, 'views/products/index.html', {'items' : context})

def new(response):

   context = {
      "navbar": navBar("products", "new"),
      'form': ProductForm,
   }
   
   return render(response, 'views/products/create.html', {'items' : context})

def store(request):

   form = ProductForm(request.POST)

   if form.is_valid():
      form.save()
   
   if not Barcode.objects.filter(barcode=request.POST['barcode']):
      newP = Product.objects.latest('id')
      barcode = Barcode()
      barcode.barcode = request.POST['barcode']
      barcode.product_id = newP.pk
      barcode.save()
   
   return redirect('/app/products')

def get_barcode(request):

   barcodes = Barcode.objects.all()

   items = []

   for b in barcodes:
      items.append(b.barcode)
   
   items = json.dumps(items)

   mimetype = 'application/json'

   return HttpResponse(items, mimetype)

def damage(response):
    pass

 