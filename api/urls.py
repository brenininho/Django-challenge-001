from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from .views import Register
# from .views import Logout

router = routers.DefaultRouter()
router.register(r'admin/authors', views.AuthorViewSet)
router.register(r'admin/articles', views.ArticleViewSet)
router.register(r'articles', views.LoggedOutArticleViewSet)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/sign-up/', Register.as_view(), name='register'),

    path("api/", include(router.urls)),
    # path('api/login2/', include('rest_framework.urls')),
    # path('api/logout/', Logout.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
