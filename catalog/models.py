from datetime import date

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=200, verbose_name='описание')


    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=200, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='product_image/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена')
    creation_date = models.DateField(default=date.today, verbose_name='дата создания', **NULLABLE)
    last_modification_date = models.DateField(default=date.today, verbose_name='дата редактирования', **NULLABLE)
    is_active = models.BooleanField(default=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=20, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.version_name}'



