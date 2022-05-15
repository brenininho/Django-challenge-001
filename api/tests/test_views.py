from django.urls import reverse
from my_challenge.models import Author, Article
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


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

        # self.res = self.client.post(self.register_url, self.user_data, format="json")
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
        data = {
            "name": "Robert Kiyosaki"
        }
        response = self.client.get(self.authors_list, data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "Robert Kiyosaki")

    def test_author_detail(self):

        response = self.client.get(self.author_detail)
        self.assertEqual(response.data["name"], "Robert Kiyosaki")

    def test_author_detail_update(self):
        data = {
            "name": "Napoleon Hill",
        }
        response = self.client.put(self.author_detail, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Napoleon Hill")

    def test_valid_delete_author(self):
        response = self.client.delete(self.author_detail)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_invalid_delete_author(self):
        response = self.client.delete(self.invalid_author_detail)
        self.assertEqual(response.status_code, 404)

    def test_article_list_GET(self):
        response = self.client.get(self.articles_list)
        self.assertEqual(response.data[0]["category"], "Finanças")

    def test_invalid_body_minimun_length(self):

        data = {
            "author_id": Author.objects.first().id,
            "category": "Finanças",
            "title": "Pai rico Pai pobre",
            "summary": "Ele advoga a busca pela independência financeira através de investimento, imóveis, ter seu próprio negócio e o uso de táticas financeiras de proteção do patrimônio.",
            "first_paragraph": "Um livro sobre como proteger seu patrimônio em vista da inflação com duas visões de negócios diferentes",
            "body": "A escola prepara as crianças para o mundo real?",

        }
        response = self.client.post(self.articles_list, data=data)
        self.assertEqual(response.status_code, 400)

    def test_body_minimun_length(self):
        data = {
            "author_id": Author.objects.first().id,
            "category": "Finanças",
            "title": "Pai rico Pai pobre",
            "summary": "Ele advoga a busca pela independência financeira através de investimento, imóveis, ter seu próprio negócio e o uso de táticas financeiras de proteção do patrimônio.",
            "first_paragraph": "Um livro sobre como proteger seu patrimônio em vista da inflação com duas visões de negócios diferentes",
            "body": "A escola prepara as crianças para o mundo real? Essa é a primeira pergunta com a qual o leitor se depara neste livro.",

        }
        response = self.client.post(self.articles_list, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["body"], data["body"])
        self.assertEquals(response.data["author"]["id"], str(data["author_id"]))

