from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer
from .models import CustomUser

class SignupView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]