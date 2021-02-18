from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['id','username','password','email']


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','password2')
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],

        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
           raise serializers.ValidationError({'password':'Passwords must macth.!'})

        user.set_password(password)
        user.save()
        return user


# class CustomSerialiser(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:

#         model = CustomUser
#         fields ='__all__'

#     def update(self, instance, validated_data):
   
#         instance.role=self.validated_data['role'],
#         instance.phone_number=self.validated_data['phone_number'],
#         instance.full_name=self.validated_data['full_name']
        
#         instance.save()
#         return instance

#     def to_internal_value(self, data):
#         user_data = data['user']
#         return super().to_internal_value(user_data)

#     def to_representation(self, instance):
#         pass
    
    
