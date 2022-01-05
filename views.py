from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import sellerSerializer
from .models import seller
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(viewsets.ModelViewSet):
    queryset = seller.objects.all()
    serializer_class = sellerSerializer
    permission_classes = [permissions.AllowAny]