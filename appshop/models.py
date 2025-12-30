from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)


class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    on_sale = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
