from django.urls import path
from .views import CaseListCreateAPIView 

urlpatterns = [
    path('cases/', CaseListCreateAPIView.as_view(), name='case-list-create')

]