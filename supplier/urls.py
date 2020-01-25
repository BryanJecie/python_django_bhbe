from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.create, name="create_supplier"),
    path("store/", views.store, name="store_supplier"),
    path("<int:id>", views.show, name="showsupplier"),
    # path("", views.show, name="show_supplier"),
]
