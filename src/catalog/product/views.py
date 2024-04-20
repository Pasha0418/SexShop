from rest_framework import generics
from catalog.models import Product, Category
from catalog.product.serializers import ListProductSerializer, DetailProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from catalog.service import ProductFilter


class ListProductSearchCategoryApiView(generics.ListAPIView):
    """Display a list of products by category and filtering products by price and rating"""
    lookup_field = 'url'
    serializer_class = ListProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        category = Category.objects.get(url=self.kwargs['url'])
        product = Product.objects.filter(category=category, active=True)
        return product


class DetailProductApiView(generics.RetrieveAPIView):
    """Full description of the product"""
    lookup_field = 'url'
    serializer_class = DetailProductSerializer
    queryset = Product.objects.filter(active=True)


class ListProductApiView(generics.ListAPIView):
    """Display a list of products and filtering products by price and rating"""
    serializer_class = ListProductSerializer
    queryset = Product.objects.filter(active=True)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter



