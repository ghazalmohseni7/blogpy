from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Article
from . import serializers

# Create your views here.

class AllArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            data = []
            all_articles = Article.objects.all().order_by('created_at')[:6]
            for article in all_articles:
                data.append(
                    {
                        'title': article.title,
                        'cover': article.cover.url if article.cover else None,
                        'category': article.category.title,
                        'author': article.author.user.username,
                        'promote': article.promote,
                        'content': article.content,
                        'created_at': article.created_at,
                    }
                )
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            article_name = request.GET['article_title']
            article = Article.objects.filter(title=article_name)
            serialized_data = serializers.SingleArticleSerializers(article, many=True)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)


        except:
            return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
