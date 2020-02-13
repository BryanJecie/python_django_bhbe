from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from utilities.helper import navBar

from .forms import SupplierForm
from .models import Supplier

from querybuilder.query import Query


def index(response):

    data = {
        "navbar": navBar("suppliers", "manage"),
        "suppliers": Supplier.objects.all(),
    }

    return render(response, "views/suppliers/index.html", {"items": data})


def create(response):

    data = {"navbar": navBar("suppliers", "new"), "newForm": SupplierForm()}

    return render(response, "views/suppliers/create.html", {"items": data})


def store(request):
    form = SupplierForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("/app/suppliers")


def show(request, code):

    supplier = Supplier.objects.get(supplier_code=code)

    data = {
        "navbar": navBar("suppliers", ""),
        "tab": request.GET.get("tab"),
        "supplier": supplier,
    }

    return render(request, "views/suppliers/show.html", {"items": data})

def edit(request, code):

    supplier = Supplier.objects.get(supplier_code=code)

    data = {
        "navbar": navBar("suppliers", ""),
        "form": SupplierForm(instance=supplier),
        "supplier": supplier,
    }

    return render(request, "views/suppliers/edit.html", {"items": data})


def distroy(request, id):

    supplier = Supplier.objects.get(id=id)

    supplier.delete()

    messages.success(request, "Supplier has successfully deleted")

    return redirect("/app/suppliers")

