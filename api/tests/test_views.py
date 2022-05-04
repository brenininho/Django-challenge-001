from .test_setup import TestSetUp
from django.test import TestCase, Client
from django.urls import reverse
import json
from my_challenge.models import Author, Article


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.authors_list = reverse('author-list')

    def test_project_list_GET(self):
        response = self.client.get(self.authors_list)
        print(response)
        self.assertEqual(response.data, {"name": "Breno"})
        # self.assertTemplateUsed(response, 'api/')

    # def test_user_cannot_register_with_no_data(self):
    #     res = self.client.post(self.register_url)
    #     self.assertEqual(res.status_code, 400)
