import uuid
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics, serializers
from rest_framework.response import Response
from .serializers import AuthorSerializer, LoggedArticleSerializer, RegisterSerializer, LoggedOutArticleSerializer
from my_challenge.models import Author, Article
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# class Logout(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ["name"]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    filterset_fields = ["author", 'category', 'title']

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return LoggedArticleSerializer
        else:
            return LoggedOutArticleSerializer
