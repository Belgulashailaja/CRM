from django.shortcuts import render
from rest_framework import generics
from .serializers import OpportunitySerializer
from .models import Opportunity

# Create your views here.
class OpportunityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
