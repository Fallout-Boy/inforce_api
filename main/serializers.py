from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant, Menu, Vote


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'
