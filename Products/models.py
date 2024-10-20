from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


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
        upload_to="products/", blank=True, null=True, default="products/default1.jpg"
    )
    image2 = models.ImageField(
        upload_to="products/", blank=True, null=True, default="products/default2.jpg"
    )
    image3 = models.ImageField(
        upload_to="products/", blank=True, null=True, default="products/default3.jpg"
    )

    def __str__(self):
        return self.title
