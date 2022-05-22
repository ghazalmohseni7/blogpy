from django.urls import path, include
from . import views
urlpatterns=[

    path('article/all/',views.AllArticleAPIView.as_view(),name='all_article'),
    path('article/',views.SingleArticleAPIView.as_view(),name='single_article'),
]