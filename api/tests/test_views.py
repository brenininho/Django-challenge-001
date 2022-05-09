from django.test import TestCase, Client
from django.urls import reverse
from my_challenge.models import Author, Article
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json


class TestViews(APITestCase):

    def setUp(self):
        # self.user = User.objects.create_user(
        #     username='admin', password='admin')
        # self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.client = Client()

        self.authors_list = reverse('author-list')

        Author.objects.bulk_create(
            [
                Author(name="Robert Kiyosaki"),
                Author(name="Breno Valle"),
                Author(name="Robert Martin"),
            ]
        )

        self.response = self.client.get(self.authors_list)

        self.author_id = self.response.data[0]["id"]

        self.author_detail = reverse('author-detail', args=[self.author_id])
        self.invalid_author_detail = reverse('author-detail', args=[5])

    def test_author_list_GET(self):
        response = self.client.get(self.authors_list)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.data[0]["name"], "Robert Kiyosaki")
        self.assertEqual(response.data[1]["name"], "Breno Valle")
        self.assertEqual(response.data[2]["name"], "Robert Martin")

    def test_author_POST(self):
        # definition
        data = {
            "name": "Robert Kiyosaki"
        }
        # process
        response = self.client.get(self.authors_list, data=data)
        # print(f'response: {response} \n response data: {response.data}')

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "Robert Kiyosaki")

    def test_author_detail(self):

        response = self.client.get(self.author_detail)
        # print("response", response.data)
        self.assertEqual(response.data["name"], "Robert Kiyosaki")

    def test_author_detail_update(self):
        data = {
            "name": "Napoleon Hill"
        }
        response = self.client.put(self.author_detail, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Napoleon Hill")

    def test_valid_delete_author(self):
        response = self.client.delete(self.author_detail)
        response_authors = self.client.get(self.authors_list)
        print(f"Response: {response.data} \n Response2: {response_authors.data}")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_invalid_delete_author(self):
        response = self.client.delete(self.invalid_author_detail)
        # response_authors = self.client.get(self.authors_list)
        # print(f"Response: {response.data} \n Response2: {response_authors.data}")
        self.assertEqual(response.status_code, 404)
