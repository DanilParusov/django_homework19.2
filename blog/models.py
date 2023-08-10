from django.db import models
from pytils.translit import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(default=slugify(str(title)))
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='Превью (изображение)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
