from django.urls import path
from blog.views import BlogCreateView, BlogDeleteView, BlogListView, BlogDetailView, BlogUpdateView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('view/<str:slug>', BlogDetailView.as_view(), name='blog_view'),
    path('edit/<str:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('delete/<str:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]