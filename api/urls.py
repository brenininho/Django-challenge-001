from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("", views.getRoutes),
    path("api/authors/", views.getAuthors),
    path("api/author/<int:id>/", views.getAuthor),
    path("api/articles/", views.getArticles),
    path("api/article/<int:id>/", views.getArticle),
]
