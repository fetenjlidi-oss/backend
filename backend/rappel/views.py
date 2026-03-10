from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import RappelSerializer    
from .serializers import RappelSerializer
from .models import Rappel 
from rest_framework import status
class RappelCreateView(APIView):
    def post(self, request):
        serializer = RappelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rappel = serializer.save()
        return Response(RappelSerializer(rappel).data, status=status.HTTP_201_CREATED) 
class RappelListView(APIView):
    def get(self, request):
        rappels = Rappel.objects.all().order_by("-id")
        serializer = RappelSerializer(rappels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class RappelDetailView(APIView):    
    def get(self, request, pk):
        try:
            rappel = Rappel.objects.get(id=pk)
        except Rappel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RappelSerializer(rappel)
        return Response(serializer.data, status=status.HTTP_200_OK)
class RappelUpdateView(APIView):
    def put(self, request, pk):
        try:
            rappel = Rappel.objects.get(id=pk)
        except Rappel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RappelSerializer(rappel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)  
    def patch(self, request,pk: int):
        rappel = get_object_or_404(Rappel, id=pk)
        serializer = RappelSerializer(rappel, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
class RappelDeleteView(APIView):    
    def delete(self, request, pk):
        try:
            rappel = Rappel.objects.get(id=pk)
        except Rappel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rappel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    




# Create your views here.
