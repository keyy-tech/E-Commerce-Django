from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ProductForm, CategoryForm
from .models import Category, Product


@login_required
def home(request):
    products = Product.objects.all()
    content = {"products": products}
    return render(request, "Products/home.html", content)


def product_view(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data.get("title")
            product_description = form.cleaned_data.get("description")
            product_price = form.cleaned_data.get("price")
            product_brand = form.cleaned_data.get("brand")

            # Check if the product already exists
            if Product.objects.filter(
                title=product_name,
                description=product_description,
                price=product_price,
                brand=product_brand,
            ).exists():
                messages.error(request, "This product already exists.")
            else:
                # Save the product
                product = form.save(commit=False)
                product.title = product_name
                product.description = product_description
                product.price = product_price
                product.brand = product_brand
                product.save()

                messages.success(request, "The product has been successfully added.")
                return redirect("add_product")
        else:
            messages.error(request, "There was an error in the form.")

    content = {"form": form}
    return render(request, "Products/add_product.html", content)


def category_view(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_title = form.cleaned_data.get("title")
            category_description = form.cleaned_data.get("description")

            # Check if the category already exists
            if Category.objects.filter(
                title=category_title,
                description=category_description,
            ).exists():
                messages.error(request, "This category already exists.")
            else:
                # Save the category
                category = form.save(commit=False)
                category.title = category_title
                category.description = category_description
                category.save()

                messages.success(request, "The category has been successfully added.")
                return redirect("add_category")
        else:
            messages.error(request, "There was an error in the form.")

    content = {"form": form}
    return render(request, "Products/add_category.html", content)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    content = {"product": product}
    return render(request, "Products/product_detail.html", content)


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    messages.success(request, "The product has been successfully deleted.")
    return redirect("home")


def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "The product has been successfully updated.")
            return redirect("home")
    content = {"form": form}
    return render(request, "Products/update_product.html", content)


def product_read(request):
    products = Product.objects.all()
    content = {"products": products}
    return render(request, "Products/read_product.html", content)
