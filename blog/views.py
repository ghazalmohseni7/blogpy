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
        all_promoted_articles = Article.objects.filter(promote=True)
        promoted_data = []
        for prArt in all_promoted_articles:
            promoted_data.append(

                {
                    'title': prArt.title,
                    'category': prArt.category.title,
                    'created_at': prArt.created_at.date(),
                    'avatr': prArt.author.avatar.url if prArt.author.avatar else None,
                    'author': prArt.author.user,
                    'cover': prArt.cover.url if prArt.cover else None,

                }
            )
        context = {
            'article_data': article_data,
            'promote_article': promoted_data,
        }
        return render(request, 'blog/index.html', context)


class contactPage(TemplateView):
    template_name = 'blog/page-contact.html'
