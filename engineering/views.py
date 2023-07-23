from django.shortcuts import render
from rest_framework import viewsets, filters, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django.http import HttpResponse
from .permission import *

from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только текущего аутентифицированного пользователя
        return User.objects.filter(pk=self.request.user.id)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact']
    }

class CategoryHotelViewSet(viewsets.ModelViewSet):
    queryset = CategoryHotel.objects.all()
    serializer_class = CategoryHotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'value': ['exact']
    }

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact'],
        'price': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'category': ['exact', 'gt', 'lt', 'gte', 'lte'],
    }

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact']
    }
    permission_classes = (IsAdminOrReadOnly, )
class LastFive(viewsets.ModelViewSet):
    queryset = Tour.objects.order_by('-created_at')[:5]
    serializer_class = TourSerializer
class Sale(viewsets.ModelViewSet):
    queryset = Tour.objects.order_by('price')[:5]
    serializer_class = TourSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset=Tour.objects.all()
    serializer_class = TourSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact'],
        'category': ['exact'],
        'price': ['exact', 'gt', 'lt', 'gte', 'lte'],
    }
    ordering_fields = ['id','title', 'price', 'created_at' ]
    ordering = ['title']
    search_fields = ['title']
    permission_classes = (IsAdminOrReadOnly, )

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backend=[DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backend=[DjangoFilterBackend]
    permission_classes = (IsOWnerOrReadOnly, )

class ClicksView(viewsets.ModelViewSet):
    queryset = Clicks.objects.all()
    serializer_class=ClickSerializer

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact'],
    }
    permission_classes = (IsAdminOrReadOnly, )

class DiyViewSet(viewsets.ModelViewSet):
    queryset = DIY.objects.all()
    serializer_class = DIY_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'customer': ['exact'],
        'country': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'attraction': ['exact'],
        'hotel': ['exact']
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только текущего аутентифицированного пользователя
        return DIY.objects.filter(id=self.request.user.id)
