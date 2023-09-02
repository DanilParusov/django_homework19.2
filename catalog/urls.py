from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductCreateView, ProductDetailView, ProductDeleteView, ProductUpdateView, \
    CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    # path('contacts/', contacts),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='product_list'),
    path('view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]