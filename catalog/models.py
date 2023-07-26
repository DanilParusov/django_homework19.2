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
    image = models.ImageField(upload_to='product_image/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    creation_date = models.DateField()
    last_modification_date = models.DateField()

    def __str__(self):
        return f'{self.name}'


