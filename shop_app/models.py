from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    price = models.FloatField(
        validators=[MinValueValidator(0), ], verbose_name='Цена')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, verbose_name='Магазин')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-title']


class Shop(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название магазина')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['title']

    def __str__(self):
        return self.title
