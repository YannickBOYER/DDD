from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..service.article_service import ArticleService

class ArticleRestController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.article_service = ArticleService()

    def get(self, request):
        articles = self.article_service.get_articles()
        return Response({"articles": articles})
    
    def post(self, request):
        return Response({"message": "POST - Création d’un article"}, status=status.HTTP_201_CREATED)
