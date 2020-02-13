from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Category, Brand

from .forms import CategoryForm


navBar = {
    "parent": "products",
    "subparent": "category",
    "child": "manage-category",
}


def index(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category has successfully Save.")
            return redirect("/app/products/category/")

    items = {
        "title": "index",
        "navbar": navBar,
        "form": {"data": CategoryForm, "route": "/app/products/category/",},
        "categories": Category.objects.all(),
    }

    return render(request, "views/category/index.html", {"items": items})


def edit(request, id):

    category = Category.objects.get(id=id)

    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        messages.success(request, "Category has successfully Updated")
        return redirect("/app/products/category/")

    items = {
        "title": "edit",
        "navbar": navBar,
        "form": {"data": form, "route": "/app/products/category/" + str(id) + "/edit",},
        "categories": Category.objects.all(),
        "category": category,
    }

    return render(request, "views/category/index.html", {"items": items})


def destroy(request, id):

    category = Category.objects.get(id=id)

    category.delete()

    messages.success(request, "Category has successfully deleted")

    return redirect("/app/products/category/")
