from django.urls import path

from apps.views import create_product

urlpatterns = [
    path('products/', create_product, name='create_product'),
]
