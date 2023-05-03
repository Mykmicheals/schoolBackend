
from django.urls import path
from .views import *

urlpatterns = [
    path('user/', get_user_details),
]
