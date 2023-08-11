
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('Menu/items', views.MenuItemsView.as_view(),name='menu-list'),
    path('Menu/item/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking', views.BookingViewSet.as_view()),
    path('auth', views.CreateUserView.as_view()),
    path('login', obtain_auth_token),
]