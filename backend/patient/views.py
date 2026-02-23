from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient
from .serializers import PatientSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter 
from allauth.socialaccount.providers.oauth2.client import OAuth2Client 
from dj_rest_auth.registration.views import SocialLoginView 
from django.conf import settings 
class PatientCreateView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()
        return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)


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



class  GoogleLogin ( SocialLoginView ): 
    adapter_class = GoogleOAuth2Adapter 
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL 
    client_class = OAuth2Client
class  GoogleLoginCallback ( APIView ): 
    def  get ( self, request, *args, **kwargs ): 
        """ 
        Si vous développez une application fullstack (par exemple, une application React en plus de Django), 
        vous pouvez placer ce point de terminaison dans votre application frontend pour 
        y recevoir les jetons JWT et les stocker dans l'état. 
        """

         code = request.GET.get( "code" ) 

        if code is  None : 
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        
        # N'oubliez pas de remplacer localhost:8000 par le nom de domaine réel avant le déploiement
         token_endpoint_url = urljoin( "http://localhost:8000" , reverse( "google_login" )) 
        response = requests.post(url=token_endpoint_url, data={ "code" : code}) 

        return Response(response.json(), status=status.HTTP_200_OK)