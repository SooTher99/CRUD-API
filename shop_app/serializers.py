from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import PasswordField, TokenObtainPairSerializer

from shop_app.models import Product
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        user_obj = User.objects.filter(email=attrs.get("username")).first() or \
                   User.objects.filter(username=attrs.get("username")).first()

        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)