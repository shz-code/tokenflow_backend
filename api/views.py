from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def index(request):
    return Response({"ok"}, status=status.HTTP_200_OK)
