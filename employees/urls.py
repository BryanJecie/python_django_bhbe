from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="manage_employee"),
    path("new/", views.create, name="new_employee"),
    path("add/", views.store, name="store_employee"),
]
