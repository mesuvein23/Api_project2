from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User    
        fields = '__all__'    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'