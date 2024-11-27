from django.db import models

class WebSite(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name='Наименование категории')

    def my_func(self):
        return "Hello from model";

    def __str__(self):
        # array = [self.title, self.content, self.created_at, self.updated_at, self.is_published]
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    def __str__(self):
        # array = [self.title, self.content, self.created_at, self.updated_at, self.is_published]
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']