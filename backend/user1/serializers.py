from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "role", "is_verified", "is_active")
        read_only_fields = ("id", "is_verified")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("id", "email", "username", "password", "first_name", "last_name", "role")
        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.setdefault("username", validated_data.get("email"))
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user