from rest_framework import serializers
from catalog.models import Category


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'url']


class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
