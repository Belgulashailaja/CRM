from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer  # Corrected serializer import name

class LeadListAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    #permission_classes = (IsAdminUser,)
class LeadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

