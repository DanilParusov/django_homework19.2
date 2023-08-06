from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f"{name} - {email} - {message}")
    return render(request, 'catalog/contacts.html')

