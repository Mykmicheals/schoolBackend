from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'is_teacher', 'is_student', 'is_principal',
                  'first_name', 'middle_name', 'last_name', 'classroom', 'gender')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            gender=validated_data['gender'],
            # Use get() to handle optional field
            classroom=validated_data.get('classroom'),
            last_name=validated_data['last_name'],
            is_student=validated_data['is_student'],
            is_teacher=validated_data['is_teacher'],
            is_principal=validated_data['is_principal'],
        )

        print(user)
        user.set_password(validated_data['password'])
        user.save()

        return user
