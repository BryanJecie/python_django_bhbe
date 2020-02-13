from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_category"),
    path("<int:id>/delete", views.destroy, name="delete_category"),
    path("<int:id>/edit", views.edit, name="edit_category"),
]

