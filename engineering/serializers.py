from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields=['title']

class CategoryHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryHotel
        fields=['value']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields=['title', 'country', 'category', 'contact', 'price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['title']
    
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields=[ 'id','title', 'country','img', 'date_of_start', 'date_of_end', 'price', 'category']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields=[ 'tour', 'book_date', 'status']
    
        def create(self, validated_data):
        # Получаем текущего пользователя, который выполнил вход (залогинился)
            user = self.context['request'].user

            validated_data['customer'] = user

            project = Booking.objects.create(**validated_data)
            return project

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields=['id', 'customer', 'tour', 'text', 'ranking']

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clicks
        fields = ['first_name', 'number']

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields=['title', 'country']

class DIY_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DIY
        fields=['customer', 'country', 'cust_number', 'date_of_start', 'date_of_end', 'attraction', 'hotel']

        def create(self, validated_data):
        # Получаем текущего пользователя, который выполнил вход (залогинился)
            user = self.context['request'].customer

            validated_data['customer'] = user

            project = DIY.objects.create(**validated_data)
            return project

