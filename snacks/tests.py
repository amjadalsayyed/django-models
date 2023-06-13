from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.
class SnacksTest(TestCase): 
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(name="ronaldo", purchaser=purchaser)

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        snacks = response.context['snacks']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0].name, "ronaldo")
        self.assertEqual(snacks[0].description, 'bla bla bla ..')
        self.assertEqual(snacks[0].purchaser.username, "tester") 

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "ronaldo")
        self.assertEqual(snack.description, 'bla bla bla ..')
        self.assertEqual(snack.purchaser.username, "tester")     
