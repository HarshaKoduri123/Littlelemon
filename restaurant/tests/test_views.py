from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(Title="Pizza", Price=12, Inventory=50)
        Menu.objects.create(Title="Burger", Price=8, Inventory=100)

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-list'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
