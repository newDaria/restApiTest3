
from django.urls import path, include
# from .views import article_list, article_detail, ArticleAPIView

from .views import  ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('article/', ArticleAPIView.as_view()),
    path('details/<int:id>', ArticleDetails.as_view()),
    path('generic/article/<int:pk>', GenericAPIView.as_view()),

]

