from urllib.parse import urljoin

from django.shortcuts import get_object_or_404
from django.urls import reverse
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Patient
from .serializers import PatientSerializer ,RegisterSerializer

from rest_framework import serializers
from django.contrib.auth import authenticate

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter 
from allauth.socialaccount.providers.oauth2.client import OAuth2Client 
from dj_rest_auth.registration.views import AllowAny, SocialLoginView 
from django.conf import settings 
class PatientCreateView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()
            return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientListView(APIView):
    def get(self, request):
        patients = Patient.objects.all().order_by("-id")
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientDetailView(APIView):
    def get(self, request, id: int):
        patient = get_object_or_404(Patient, id=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientUpdateView(APIView):
    def put(self, request, id: int):
        patient = get_object_or_404(Patient, id=id)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id: int):
        patient = get_object_or_404(Patient, id=id)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientDeleteView(APIView):
    def delete(self, request, id: int):
        patient = get_object_or_404(Patient, id=id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
class PatientLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        patient = serializer.validated_data["patient"]

        refresh = RefreshToken.for_user(patient)  # type: ignore

        return Response(
            {
                "patient": PatientSerializer(patient).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
