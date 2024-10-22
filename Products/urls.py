from django.urls import path
from Products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.home, name="home"),
    path("add_product/", views.product_view, name="add_product"),
    path("add_category/", views.category_view, name="add_category"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("read/", views.product_read, name="read"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
