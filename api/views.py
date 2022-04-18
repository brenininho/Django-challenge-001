from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthorSerializer, ArticleSerializer
from my_challenge.models import Author, Article


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"POST": "/api/projects/id/vote"},

        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
    ]
    return Response(routes)


@api_view(["GET"])
def getAuthors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAuthor(request, id):
    author = Author.objects.get(id=id)
    serializer = AuthorSerializer(author, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getArticles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getArticle(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)
