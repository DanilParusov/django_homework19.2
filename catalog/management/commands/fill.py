from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'car', 'description': 'about'},
            {'name': 'phone', 'description': 'about'},
            {'name': 'laptop', 'description': 'about'},
            {'name': 'house', 'description': 'about'}
        ]

        product_list = [
            {'name': 'bmw', 'category': 'car', 'price': '2000', 'description': 'Hellow sddddddddddddddddddddfffffffffsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'},
            {'name': 'iphone', 'category': 'phone', 'price': '2000'},
            {'name': 'lenovo', 'category': 'laptop', 'price': '2000'},
            {'name': 'villa', 'category': 'house', 'price': '500000'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product_item in product_list:
            category_name = product_item.pop('category')
            category = Category.objects.get(name=category_name)
            product_item['category'] = category
            product_for_create.append(Product(**product_item))

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)



