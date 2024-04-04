# serializers.py
from rest_framework import serializers
from ecomApp.models import CustomUser
# class RegistrationSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     otp = serializers.CharField()
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('phone_number',  'password','name')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'required': False},
            'phone_number': {'required': False},
            'email': {'required': False},
        }


from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
