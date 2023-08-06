from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from blog.models import BlogPost
from django.urls import reverse_lazy

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blogpost:list')

class BlogListView(ListView):
    model = BlogPost


class BlogDetailView(DetailView):
    model = BlogPost

class BlogDeleteView(DeleteView):
    pass

class BlogUpdateView(UpdateView):
    pass


