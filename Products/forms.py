from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "stock_quantity",
            "brand",
            "weight",
            "image1",
            "image2",
            "image3",
            "category",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-floating", "placeholder": "Product Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-floating", "placeholder": "Product Description"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-floating", "placeholder": "Product Price"}
            ),
            "stock_quantity": forms.NumberInput(
                attrs={"class": "form-floating", "placeholder": "Stock Quantity"}
            ),
            "brand": forms.TextInput(
                attrs={"class": "form-floating", "placeholder": "Brand"}
            ),
            "weight": forms.NumberInput(
                attrs={"class": "form-floating", "placeholder": "Weight"}
            ),
            "category": forms.Select(
                attrs={"class": "form-floating", "placeholder": "Category"}
            ),
            "image1": forms.FileInput(
                attrs={"class": "form-floating", "placeholder": "Image 1"}
            ),
            "image2": forms.FileInput(
                attrs={"class": "form-floating", "placeholder": "Image 2"}
            ),
            "image3": forms.FileInput(
                attrs={"class": "form-floating", "placeholder": "Image 3"}
            ),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title", "description"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-floating", "placeholder": "Category Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-floating", "placeholder": "Category Description"}
            ),
        }
