from django.db import models
from authentication.models import User
from catalog.models import Product
import uuid


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket', null=True, blank=True)

    def __str__(self):
        return f"Cart for  user '{self.user.username}' "


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Item with Product {self.product.name} user '{self.cart.user.username}' quantity = {self.quantity} "

