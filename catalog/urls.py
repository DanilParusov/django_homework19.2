from django.urls import path

from catalog.views import contacts, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', contacts),
    path('detail/<int:pk>/', ProductDetailView.as_view())
]