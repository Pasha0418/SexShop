from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    """Filtering products by price and rating """
    price = filters.RangeFilter()
    rating = filters.CharFilter(field_name='rating__value', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['price', 'rating']