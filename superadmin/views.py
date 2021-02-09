from django.shortcuts import render

# ***************** API ****************
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets



# Create your views here.

class ProfileView(APIView):
    pass