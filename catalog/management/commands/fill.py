from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'car','description': 'about'},
            {'name': 'phone', 'description': 'about'},
            {'name': 'laptop', 'description': 'about'},
            {'name': 'house', 'description': 'about'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)
