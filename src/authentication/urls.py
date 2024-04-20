from django.urls import path
from .views import ActivateUserApiView

urlpatterns = [
    path('users/activate/<str:uid>/<str:token>/', ActivateUserApiView.as_view()),
]
