from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        user_data = {
            'username': 'username',
            'password': 'password'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
