from rest_framework.generics import *
from .models import Student
from .serilizer import StudentSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Students(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    

    # permission_classes = [permissions.IsAdminUser]
   # permission_classes = [permissions.IsAuthenticated]

class StudentCreateView(CreateAPIView):
    serializer_class = StudentSerializer


    

