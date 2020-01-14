from django.shortcuts import render
from django.http import HttpResponse


def index(response):

    return render(response, 'views/users/index.html')
