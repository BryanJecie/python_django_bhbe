from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
    path("", views.index, name="manage_products"),
    path("new/", views.new, name="create_products"),
    path("post/", views.store, name="store_products"),
    path("damage/", views.damage, name="damage_products"),
    url(r"^category/", include("category.urls")),
    url(r"^brands/", include("category.brands.urls")),
    url(r'^getbarcode/$', views.get_barcode, name='load_barcode'),
]
