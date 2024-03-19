from django.urls import path
from .views import DocumentListCreateAPIView

urlpatterns = [
    path('documents/', DocumentListCreateAPIView.as_view(), name='document-list-create')

]