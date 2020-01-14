from django.shortcuts import render
from django.http import HttpResponse
from .models import Personnel, Contact


def index(response):

    return render(response, 'main/content/home.html')


# def contact(response):
#     p = Personnel.objects.get(id=1)

#     return render(response, 'pages/home.html', {'data': p})

#     # return HttpResponse('<h1>This is contact Area</h1>')


# # for users pages
# def users(response):
#     users = User.objects.get()

#     return render(response, 'pages/users/index.html', {'users': users})
