# filehandler/views.py
from django.http import HttpResponse
from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer

def home(request):
    return HttpResponse("Welcome to the File API!")

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
