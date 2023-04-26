from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'is_teacher', 'is_student', 'is_principal')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            is_student=validated_data['is_student'],
            is_teacher=validated_data['is_teacher'],
            is_principal=validated_data['is_principal'],  
        )
        user.set_password(validated_data['password'])
        user.save()
        return user