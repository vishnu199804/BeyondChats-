from django.urls import path
from .views import (
    ArticleListCreateAPIView,
    ArticleRetrieveUpdateDeleteAPIView,
)

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view()),
    path("articles/<int:pk>/", ArticleRetrieveUpdateDeleteAPIView.as_view()),
]
