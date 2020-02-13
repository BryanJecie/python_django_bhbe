from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_brands"),
    path("<int:id>/edit", views.edit, name="edit_brand"),
    path("<int:id>/delete", views.destroy, name="delete_brand"),
]

