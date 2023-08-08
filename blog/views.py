from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from pytils.translit import slugify

from blog.models import BlogPost
from django.urls import reverse_lazy, reverse

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('blogpost:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post_slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

class BlogListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:blog_list')

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview']

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
            self.kwargs['slug'] = new_post.slug

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogpost:blog_view', args=[self.kwargs.get('slug')])


