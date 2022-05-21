from django.urls import path, include
from . import views
urlpatterns=[

    path('article/all/',views.AllArticleAPIView.as_view(),name='all_article'),
]