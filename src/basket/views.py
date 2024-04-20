from rest_framework import permissions, views
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import Response, status
from .models import Cart, CartItems
from .serializers import CartSerializer, AddCartItemSerializer, UpdateCartItemSerializer, CartItemSerializer
from drf_yasg.utils import swagger_auto_schema


class UidCartUserApiView(views.APIView):
    """To find out the uid of your basket """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user.pk
        cart_uid = Cart.objects.get(user=user).id

        return Response(data={'cart-uid': f'{cart_uid}'}, status=status.HTTP_200_OK)


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):

    permission_classes = [permissions.IsAuthenticated,]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    """To find out the uid of your basket """
    permission_classes = [permissions.IsAuthenticated, ]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return CartItems.objects.filter(cart_id=self.kwargs["cart_pk"])

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    @swagger_auto_schema(
        operation_description="Display all products in the user's basket ",
        responses={200: 'OK'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Adding an item to cart by its name ",
        request_body=AddCartItemSerializer,
        responses={201: 'Created'}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Display of a specific product in the user's basket",
        responses={200: 'OK'}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     operation_description="Changing the quantity of a particular item in the user's basket",
    #     request_body=UpdateCartItemSerializer,
    #     responses={200: 'OK'}
    # )
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Changing the quantity of a particular item in the user's basket",
        request_body=UpdateCartItemSerializer,
        responses={200: 'OK'}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleting a specific item from the basket ",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_context(self):
        cart_pk = self.kwargs.get("cart_pk")
        cartitem_pk = self.kwargs.get("pk")
        return {"cart_id": cart_pk, "cartitem_id": cartitem_pk}




