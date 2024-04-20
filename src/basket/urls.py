from django.urls import path, include
from basket import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("carts", views.CartViewSet)
cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename="cart-items")
urlpatterns = [
    path("", include(cart_router.urls)),
    path("cart-uid/", views.UidCartUserApiView.as_view()),
]