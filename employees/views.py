from django.shortcuts import render
from django.http import HttpResponse
from . import forms

from utilities.helper import navBar


# from .models import models


def index(response):
    context = {"navbar": navBar("employees", "manage")}

    return render(response, "views/employees/index.html", {"context": context})


def create(response):

    context = {
        "navbar": navBar("employees", "new"),
        "form": forms.CreateNewEmployeeForm(),
    }

    return render(response, "views/employees/create.html", {"context": context})


def store(request):
    return HttpResponse(request.POST["employeeCode"])
    # return {"name": "test"}
