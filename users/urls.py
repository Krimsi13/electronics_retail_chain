from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import UserCreateApiView, UserRetrieveApiView, UserUpdateApiView, UserDestroyApiView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path("<int:pk>/", UserRetrieveApiView.as_view(), name="users_retrieve"),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users_update"),
    path("<int:pk>/delete/", UserDestroyApiView.as_view(), name="users_delete"),
    ]
