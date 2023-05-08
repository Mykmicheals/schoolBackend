from rest_framework import serializers
from django.contrib.auth.models import User
from userauth.models import CustomUser
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name',
                  'is_teacher', 'is_student', 'is_principal']


class StuentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    classroom = serializers.CharField(source='user.classroom')
    gender = serializers.CharField(source='user.gender')

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name',
                  'email', 'classroom', 'gender']


class TeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    gender = serializers.CharField(source='user.gender')

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name',
                  'email', 'gender']
        
class SubjectSerializer (serializers.ModelSerializer):
    class_offered = serializers.PrimaryKeyRelatedField(
        queryset=ClassRoom.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all())

    class Meta:
        model = Subjects
        fields = ['id', 'name', 'class_offered', 'teacher']
