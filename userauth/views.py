from rest_framework_jwt.views import ObtainJSONWebToken
from django.conf import settings
from rest_framework.response import Response
import jwt
from rest_framework import generics, status
from .serializer import UserSerializer


class CustomObtainJWT(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainJWT, self).post(request, *args, **kwargs)
        if response.status_code == 200:
            token = response.data['token']
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return Response({'token': token, 'status': 'success', 'username': decoded_token['username']})
        else:
            return Response({'status': 'error', 'message': 'Invalid credentials'})




class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
