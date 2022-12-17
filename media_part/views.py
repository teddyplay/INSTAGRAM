from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.decorators import APIView




# class PostViewSet(viewsets.ModelViewSet):
#     queryset =