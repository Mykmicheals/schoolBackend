
from django.urls import path
from .views import *

urlpatterns = [
    path('user/', get_user_details),
    path('students/',StudentListView.as_view()),
    path('teachers/', TeacherListView.as_view()),
    path('subjects/', SubjectListCreateAPIView.as_view()),
    path('mysubjects/', TeacherSubjectsListAPIView.as_view()),

]
