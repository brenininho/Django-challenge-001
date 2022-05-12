from django.test import TestCase, Client
from django.urls import reverse
from my_challenge.models import Author, Article
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json


class TestViews(APITestCase):
    register_url = reverse("register")
    login_url = reverse("login")
    user_data = {
        "email": "admin@admin.com",
        "username": "admin",
        "password": "admin",
    }

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        # self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # self.client = Client()

        self.res = self.client.post(self.register_url, self.user_data, format="json")
        self.login_response = self.client.post(self.login_url, self.user_data, format="json")
        self.token = self.login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.authors_list = reverse('author-list')
        self.articles_list = reverse("article-list")

        Author.objects.bulk_create(
            [
                Author(name="Robert Kiyosaki"),
                Author(name="Breno Valle"),
                Author(name="Robert Martin"),
            ]
        )
        #python manage.py test
        self.response = self.client.get(self.authors_list)

        self.author_id = self.response.data[0]["id"]

        self.author_detail = reverse('author-detail', args=[self.author_id])
        self.invalid_author_detail = reverse('author-detail', args=[5])

        Article.objects.bulk_create(
            [
                Article(author_id=Author.objects.first().id,
                        category="Finanças",
                        title="Pai rico Pai pobre",
                        summary="""Ele advoga a busca pela independência financeira através de investimento, imóveis,
                         ter seu próprio negócio e o uso de táticas financeiras de proteção do patrimônio.""",
                        first_paragraph="""Um livro sobre como proteger seu patrimônio em vista da inflação
                         com duas visões de negócios diferentes""",
                        body="""A escola prepara as crianças para o mundo real?""",
                        # body="""A escola prepara as crianças para o mundo real? Essa é a primeira
                        # pergunta com a qual o leitor se depara neste livro."""
                        )
            ]
        )

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
        # print(f"Response: {response.data} \n Response2: {response_authors.data}")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_invalid_delete_author(self):
        response = self.client.delete(self.invalid_author_detail)
        # response_authors = self.client.get(self.authors_list)
        # print(f"Response: {response.data} \n Response2: {response_authors.data}")
        self.assertEqual(response.status_code, 404)

    def test_article_list_GET(self):
        response = self.client.get(self.articles_list)
        # print("data: ", response.data)
        self.assertEqual(response.data[0]["category"], "Finanças")

    def test_body_minimun_length(self):


        data = {
            "author": Author.objects.first().id,
            "category": "Finanças",
            "title": "Pai rico Pai pobre",
            "summary": "Ele advoga a busca pela independência financeira através de investimento, imóveis, ter seu próprio negócio e o uso de táticas financeiras de proteção do patrimônio.",
            "first_paragraph": "Um livro sobre como proteger seu patrimônio em vista da inflação com duas visões de negócios diferentes",
            "body": "123456789",

        }
        # body="""A escola prepara as crianças para o mundo real? Essa é a primeira
            # pergunta com a qual o leitor se depara neste livro."""
        import ipdb;ipdb.set_trace()
        response = self.client.post(self.articles_list, data=data)
        print("data", response.status_code)
        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["body"], data["body"])
        self.assertEquals(response.data["author"], Author.objects.first().id)


