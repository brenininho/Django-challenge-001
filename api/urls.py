from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes),
    path("authors/", views.getAuthors),
    path("authors/<int:id>/", views.getAuthor),
    path("articles/", views.getArticles),
    path("articles/<int:id>/", views.getArticle),
]
