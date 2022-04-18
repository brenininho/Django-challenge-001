from rest_framework import serializers
from my_challenge.models import Author, Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False)
    category = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"
