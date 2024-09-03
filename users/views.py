from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer


class UserCreateApiView(CreateAPIView):
    """Регистрация пользователя."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(RetrieveAPIView):
    """Класс для получения пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):
    """Класс для изменения пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(DestroyAPIView):
    """Класс для удаления пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
