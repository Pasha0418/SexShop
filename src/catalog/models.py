from django.db import models
from authentication.models import User
from django_countries.fields import CountryField


class Product(models.Model):
    name = models.CharField(max_length=150)
    EAN = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True, db_index=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)
    colors = models.ManyToManyField('Color')
    country = CountryField()
    active = models.BooleanField(default=True)
    rating = models.ForeignKey('Star', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    with_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='field may be empty')
    material = models.ManyToManyField('Material')
    length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.IntegerField()
    time_work = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True, db_index=True)

    def __str__(self):
        return f"Category - {self.name}"


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Brand - {self.name}"


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Brand - {self.name}"


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Material - {self.name}"


class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to="product_images/")


class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    star = models.ForeignKey('Star', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Review user - {self.user.email} Product - {self.product.name}"


class Star(models.Model):
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.value}"

