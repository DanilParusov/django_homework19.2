from datetime import date

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
    creation_date = models.DateField(default=date.today, verbose_name='дата создания')
    last_modification_date = models.DateField(default=date.today, verbose_name='дата редактирования')

    def __str__(self):
        return f'{self.name}'


