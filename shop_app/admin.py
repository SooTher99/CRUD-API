from django.contrib import admin
from .models import Product, Shop

class ProductAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'shop', 'price', 'quantity')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('title', 'shop')


class ShopAdmin (admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)