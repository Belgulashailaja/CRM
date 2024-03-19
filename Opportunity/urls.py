from django.urls import path
from .views import OpportunityListCreateAPIView

urlpatterns = [
    path('opportunities/', OpportunityListCreateAPIView.as_view(), name='opportunity-list-create'),

]
