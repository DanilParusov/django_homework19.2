from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f"{name} - {email} - {message}")
    return render(request, 'catalog/contacts.html')

def product_detail(request, object_id):
    product = Product.objects.filter(id=object_id)
    context = {
        'object': product
    }
    return render(request, 'catalog/product_detail.html', context)