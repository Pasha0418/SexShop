from rest_framework import serializers
from catalog.models import Product, Review, Image, Color


class RecursiveImageSerializer(serializers.ModelSerializer):
    """Recursive display of image"""
    class Meta:
        model = Image
        fields = ['image']


class RecursiveReviewSerializer(serializers.ModelSerializer):
    """Recursive display of reviews with get of the user"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ['text', 'star', 'user']


class RecursiveColorSerializer(serializers.ModelSerializer):
    """Recursive display of color"""
    class Meta:
        model = Color
        fields = ['name']


class ListProductSerializer(serializers.ModelSerializer):
    image = RecursiveImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'with_discount', 'image', 'url']


class DetailProductSerializer(serializers.ModelSerializer):
    image = RecursiveImageSerializer(many=True)
    review = RecursiveReviewSerializer(many=True)
    colors = RecursiveColorSerializer(many=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    material = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    rating = serializers.SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = Product
        exclude = ['active', 'url', 'created_at', 'updated_at']
