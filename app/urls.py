
from django.urls import path
from .views import *

urlpatterns = [
    path('students', Students.as_view()),
    path('addstudent', StudentCreateView.as_view()),
   
      
]
