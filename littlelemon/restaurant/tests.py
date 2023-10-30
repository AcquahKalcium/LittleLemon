from django.test import Client, TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
# from restaurant.views import MenuItemsView
from rest_framework.test import APIClient
 


#Test case Class
class MenuTest(TestCase):
    def test_get_item(self):
        instance = Menu.objects.create(id=1, title='IceCream', price=80, inventory=100)
        self.assertEqual(str(instance), 'IceCream : 80')

# This view Testclass need to be checked later
class MenuItemsViewTest(TestCase):
    def setup(self):
        self.client = APIClient
        menu_item0 = Menu.objects.create(title='Beef', price=99, inventory=200)
    def test_getall(self):
        response = self.client.get('')
        menu_items = Menu.objects.all() # gets a queryset of all 'Menu' objects from the database
        serializer = MenuSerializer(menu_items, many = True) # serializes the queryset of 'Menu' objects into a JSON-like format
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 404)
        
        
        
