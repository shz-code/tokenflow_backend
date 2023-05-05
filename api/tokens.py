from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    return Response({"ok"}, status=status.HTTP_200_OK)
