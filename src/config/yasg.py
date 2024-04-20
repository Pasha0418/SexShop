from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django SexShop",
        default_version="v1",
        description="This is the API of a simple internet sex shop. With auntefication and mail checking using Djoser library. I think this code will be useful for frontend developers to create their own projects. ",
        license=openapi.License(name='BSD Licence'),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]