from django.urls import path
from .views import home, add_category, add_product

urlpatterns = [
    path("", home, name="home"),
    path("add_category/", add_category, name="add_category"),
    path("add_product/", add_product, name="add_product"),
]
