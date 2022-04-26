import uuid
from rest_framework import viewsets, status, generics, serializers
from rest_framework.response import Response
from .serializers import AuthorSerializer, ArticleSerializer, RegisterSerializer, LoggedOutArticleSerializer
from my_challenge.models import Author, Article
from rest_framework.permissions import IsAuthenticated


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

        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ArticleSerializer
        else:
            return LoggedOutArticleSerializer
