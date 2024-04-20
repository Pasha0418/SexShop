from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Material, Category, Review, Star, Image, Brand, Color


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    prepopulated_fields = {"url":("name",)}


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"url":("name",)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ['value']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_display']
    readonly_fields = ['image_display']

    def image_display(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" />')

    image_display.allow_tags = True
