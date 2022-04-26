from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from .views import Register

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/sign-up/', Register.as_view(), name='register'),

    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
