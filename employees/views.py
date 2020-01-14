from django.shortcuts import render
from . import forms


def index(response):
    context = {
        'navbar': navBar('employees', 'manage')
    }
    return render(response, 'views/employees/index.html', {'context': context})


def create(response):

    context = {
        'navbar': navBar('employees', 'new'),
        'form': forms.CreateNewEmployeeForm()
    }

    return render(response, 'views/employees/create.html', {'context': context})


def navBar(parent, child):

    return {
        'parent': parent,
        'child': {
            'manage': True if child == 'manage' else False,
            'new': True if child == 'new' else False
        }
    }
