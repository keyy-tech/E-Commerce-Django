from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def default_image_picture():
    return "products/default.png"


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)  # Adjusted
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=120)
    weight = models.DecimalField(decimal_places=2, max_digits=10)  # Adjusted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(
        upload_to="products/", blank=True, null=True, default=default_image_picture
    )
    image2 = models.ImageField(
        upload_to="products/", blank=True, null=True, default=default_image_picture
    )
    image3 = models.ImageField(
        upload_to="products/", blank=True, null=True, default=default_image_picture
    )

    def __str__(self):
        return self.title
