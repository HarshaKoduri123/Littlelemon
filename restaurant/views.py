from .serializers import BookingSerializer,MenuSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import generics
from .models import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class CreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer