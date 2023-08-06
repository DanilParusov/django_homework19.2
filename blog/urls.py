from django.urls import path
from blog.views import BlogCreateView, BlogDeleteView, BlogListView, BlogDetailView, BlogUpdateView

urlpatterns = [
    path('create/', BlogCreateView.as_view()),
    path('', BlogListView.as_view()),
    path('view/<slug:slug>', BlogDetailView.as_view()),
    path('edit/<int:pk>', BlogUpdateView.as_view()),
    path('delete/<int:pk>', BlogDeleteView.as_view()),
]