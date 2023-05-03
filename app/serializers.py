from rest_framework import serializers
from django.contrib.auth.models import User
from userauth.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','first_name','is_teacher','is_student','is_principal'] 
