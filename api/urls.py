from django.urls import path, include
from . import views

urlpatterns = [

    path('article/all/', views.AllArticleAPIView.as_view(), name='all_article'),
    path('article/', views.SingleArticleAPIView.as_view(), name='single_article'),
    path('article/submit/', views.SubmitArticleAPIView.as_view(), name='submit_article'),
    path('category/submit/', views.SubmitCategoryAPIView.as_view(), name='submit_category'),
    path('article/update', views.UpdateArticleAPIView.as_view(), name='update_article'),
    path('article/delete', views.DeleteArticleAPIView.as_view(), name='delete_article'),
]
