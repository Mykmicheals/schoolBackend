from django.urls import path
from .views import *

urlpatterns = [
     path('login', CustomObtainJWT.as_view(), name='token_obtain_pair'),
     path('signup', SignupView.as_view(), name='signup'),

]
