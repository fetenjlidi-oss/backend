from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()




class UserCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all().order_by("-id")
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


class UserUpdateView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)