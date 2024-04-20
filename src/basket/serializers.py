from rest_framework import serializers
from catalog.models import Product
from .models import Cart, CartItems


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","name", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name="total")

    class Meta:
        model = CartItems
        fields = ["id", "cart", "product", "quantity", "sub_total"]

    def total(self, cartitem: CartItems):
        return cartitem.quantity * cartitem.product.price


class AddCartItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField()
    # quantity = serializers.IntegerField()

    class Meta:
        model = CartItems
        fields = ['product']

    def validate_product_url(self, value):
        if not Product.objects.filter(url=value).exists():
            raise serializers.ValidationError("There is no product associated with the given ID")

        return value

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_name = self.validated_data["product"]
        # quantity = self.validated_data["quantity"]

        try:
            cartitem = CartItems.objects.get(product__name=product_name, cart_id=cart_id)

            cartitem.quantity += 1
            cartitem.save()

            self.instance = cartitem
        except:
            product = Product.objects.get(name=product_name)
            self.instance = CartItems.objects.create(cart_id=cart_id, product=product, quantity=1)

        return self.instance


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ["quantity"]

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        cartitem_id = self.context["cartitem_id"]
        quantity = self.validated_data["quantity"]

        cartitem = CartItems.objects.get(id=cartitem_id, cart_id=cart_id)
        cartitem.quantity += quantity
        cartitem.save()

        self.instance = cartitem

        return self.instance


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ["id", "items", "grand_total"]

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total