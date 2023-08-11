from rest_framework import serializers
from .models import Booking, Menu
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
            'password': {'write_only': True, 'required': True}
        }


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'Name', 'No_of_guests', 'BookingDate']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Inventory', 'Price']
