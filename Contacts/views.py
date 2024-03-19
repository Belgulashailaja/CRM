from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import contactSerializer  # Corrected serializer import name

class contactListAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer
    #permission_classes = (IsAdminUser,)
class contactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer
