from django.shortcuts import render, redirect
from django.http import HttpResponse

from utilities.helper import navBar

from .forms import SupplierForm

from .models import Supplier

# from .models import Supplier


def index(response):

    data = {
        "navbar": navBar("suppliers", "manage"),
        "suppliers": Supplier.objects.all(),
    }

    return render(response, "views/suppliers/index.html", {"items": data})


def create(request):

    data = {"navbar": navBar("suppliers", "new"), "newForm": SupplierForm()}

    return render(request, "views/suppliers/create.html", {"items": data})


def store(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/app/suppliers")


def show(request, id):

    supplier = Supplier.objects.get(id=id)

    data = {
        "navbar": navBar("suppliers", "new"),
        "form": SupplierForm(instance=supplier),
        "supplier": supplier,
    }

    return render(request, "views/suppliers/show.html", {"items": data})

    # for target_list in expression_list:
    #     pass

    # return HttpResponse(supplier)
