from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Article, Author
from .serializers import ArticleSerializer

"""
https://webdevblog.ru/sozdanie-django-api-ispolzuya-django-rest-framework-apiview/
APIView
GenericAPIView
ViewSets
"""

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
