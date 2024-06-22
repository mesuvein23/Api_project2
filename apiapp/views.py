from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ContactDataListCreate(ListCreateAPIView):
    serializer_class = ContactDataSerializer
    queryset = ContactData.objects.all()
    # permission_classes = [IsAuthenticated]

class ContactDataRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactDataSerializer
    queryset = ContactData.objects.all()
    # permission_classes = [IsAuthenticated]


class CategoryListCreate(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
