from rest_framework import serializers
from users.models import Pay
from rest_framework.serializers import ModelSerializer
from users.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token["username"] = user.username
        token["email"] = user.email
        return token
