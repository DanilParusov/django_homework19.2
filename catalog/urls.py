from django.urls import path

from catalog.views import index, contacts, product_detail

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('detail', product_detail)
]