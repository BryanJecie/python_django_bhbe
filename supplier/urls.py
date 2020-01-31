from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.create, name="create_supplier"),
    path("store/", views.store, name="store_supplier"),
    path("<str:code>", views.show, name="show_supplier"),
    path("<str:code>/edit/", views.edit, name="edit_supplier"),
    path("<int:id>/delete/", views.distroy, name="delete_supplier"),
    # path("", views.show, name="show_supplier"),
]
