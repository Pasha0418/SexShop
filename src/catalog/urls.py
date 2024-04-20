from django.urls import path
from catalog.product import views as view_product
from catalog.category import views as view_cat
urlpatterns = [
    path('product/list/', view_product.ListProductApiView.as_view()),
    path('product/list/<str:url>/', view_product.ListProductSearchCategoryApiView.as_view()),
    path('product/detail/<str:url>/', view_product.DetailProductApiView.as_view()),
    path('category/list/', view_cat.ListCategoryApiView.as_view()),
    path('category/detail/<str:url>/', view_cat.DetailCategoryApiView.as_view()),

]
