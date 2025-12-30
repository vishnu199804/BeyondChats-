from rest_framework import generics, viewsets
from .models import Article
from .serializers import ArticleSerializer


# GET all articles + POST
class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer


# GET / UPDATE / DELETE single article
class ArticleRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# Optional: ViewSet (for router usage)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
