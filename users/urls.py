from users.apps import UsersConfig
from users.views import (
    PayCreateAPIView,
    PayListAPIView,
    PayRetrieveAPIView,
    PayUpdateAPIView,
    PayDestroyAPIView,
    MyTokenObtainPairView,
)
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import UserCreateAPIView
from rest_framework.permissions import AllowAny


app_name = UsersConfig.name


urlpatterns = [
    path("pay/create/", PayCreateAPIView.as_view(), name="pay-create"),
    path("pay/", PayListAPIView.as_view(), name="pay-list"),
    path("pay/<int:pk>/", PayRetrieveAPIView.as_view(), name="pay-get"),
    path("pay/update/<int:pk>/", PayUpdateAPIView.as_view(), name="pay-update"),
    path("pay/delete/<int:pk>/", PayDestroyAPIView.as_view(), name="pay-delete"),
    path("login/", MyTokenObtainPairView.as_view(), name="login"),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("pay/", PayCreateAPIView.as_view(), name="pay"),
]
