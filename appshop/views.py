from django.shortcuts import render
from .models import Product, Category


def home(request):
    all_product = Product.objects.all()
    return render(request, "home.html", {"product": all_product})


def add_category(request):
    categorys = Category.objects.all()
    if request.method == "GET":
        return render(request, "add_category.html", {"categorys": categorys})

    elif request.method == "POST":
        title = request.POST.get("title")
        Category.objects.create(title=title)
        categorys = Category.objects.all()

    return render(request, "add_category.html", {"categorys": categorys})


def add_product(request):
    categorys = Category.objects.all()
    if request.method == "GET":
        return render(request, "add_product.html", {"categorys": categorys})

    elif request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        on_sale = request.POST.get("on_sale")
        id_i = request.POST.get("categorys")
        category_a = Category.objects.get(id=id_i)

        Product.objects.create(
            name=name, price=price, on_sale=on_sale, category=category_a
        )

        return render(request, "add_product.html", {"categorys": categorys})
