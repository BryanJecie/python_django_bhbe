from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from category.forms import BrandForm
from category.models import Brand

navBar = {"parent": "products", "subparent": "category", "child": "manage-brands"}

def index(request):

   if request.method == 'POST':
      form = BrandForm(request.POST)
      if form.is_valid():
         form.save(commit=request)
         messages.success(request, "Brand has successfully Save")
         return redirect('/app/products/brands/')


   items = {
      "title": "index",
      "navbar": navBar,
      "form": {
         'data': BrandForm,
         'route' : '/app/products/brands/'
      },
      'brands' : Brand.objects.all()}

   return render(request, "views/brands/index.html", {"items": items})

def edit(request, id):
   
   brand = Brand.objects.get(id=id)

   form = BrandForm(request.POST or None, instance=brand)

   if form.is_valid():
      form.save()
      messages.success(request, "Brand has successfully Updated")
      return redirect("/app/products/brands/")


   items = {
      "title": "edit",
      "navbar": navBar,
      "form": {
         'data': form,
         'route' : '/app/products/brands/' + str(id) +'/edit'
      },
      'brand' : brand,
      'brands': Brand.objects.all(),
   }

   return render(request, "views/brands/index.html", {"items": items})


def destroy(request, id):

   brand = Brand.objects.get(id=id)
   
   brand.delete()

   messages.success(request, "Brand has successfully Deleted")

   return redirect('/app/products/brands')


