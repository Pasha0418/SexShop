from rest_framework import generics
from catalog.models import Category, Product
from catalog.category.serializers import ListCategorySerializer, DetailCategorySerializer


class DetailCategoryApiView(generics.RetrieveAPIView):
    """Full description of the category """
    lookup_field = 'url'
    serializer_class = DetailCategorySerializer
    queryset = Category.objects.all()


class ListCategoryApiView(generics.ListAPIView):
    """Display a list of category """
    serializer_class = ListCategorySerializer
    queryset = Category.objects.all()