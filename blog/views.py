from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


# Create your views here.

class IndexPage(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request, **kwargs):
        all_articles = Article.objects.all().order_by('-created_at')[:6]
        article_data = []
        for article in all_articles:
            article_data.append(
                {
                    'title': article.title,
                    'category': article.category.title,
                    'created_at': article.created_at,
                    'cover': article.cover.url,

                }
            )
        context={'article_data':article_data}
        return render(request,'blog/index.html',context)
