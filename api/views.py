from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Article,userProfile,Category
from . import serializers
from django.contrib.auth.models import User
import re
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
            print(request)
            article_name = request.GET['article_title']
            article = Article.objects.filter(title=article_name)
            serialized_data = serializers.SingleArticleSerializers(article, many=True)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)


        except:
            return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # def post(self, request, format=None):
    #     try:
    #         print(request)
    #         article_name = request.GET['article_title']
    #         article = Article.objects.filter(title=article_name)
    #         serialized_data = serializers.SingleArticleSerializers(article, many=True)
    #         data = serialized_data.data
    #         return Response({'data': data}, status=status.HTTP_200_OK)
    #
    #
    #     except:
    #         return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # def post(self, request, format=None):
    #     try:
    #         print(request)
    #         article_name = request.GET['article_title']
    #         promote=request.GET['promote']
    #         print(article_name,promote)
    #         article = Article.objects.filter(title=article_name).filter(promote=promote)
    #         serialized_data = serializers.SingleArticleSerializers(article, many=True)
    #         data = serialized_data.data
    #         return Response({'data': data}, status=status.HTTP_200_OK)
    #
    #
    #     except:
    #         return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class SubmitArticleAPIView(APIView):
#     def post(self,request,format=None):
#         try:
#             serialized_data_from_user=serializers.SubmitArticleSerializer(data=request.data)
#             print((serialized_data_from_user.is_valid()))
#             print((serialized_data_from_user.errors))
#
#             if serialized_data_from_user.is_valid():
#                 print('qqqqqqqqqqqq')
#                 title=serialized_data_from_user.data.get('title')
#                 #cover = request.FILES['cover']
#                 content = serialized_data_from_user.data.get('content')
#                 # category_id = serialized_data_from_user.data.get('category_id')
#                 # author_id = serialized_data_from_user.data.get('author_id')
#                 promote = serialized_data_from_user.data.get('promote')
#                 # category= serialized_data_from_user.data.get('category')
#                 author_id= serialized_data_from_user.data.get('author')
#
#             else:
#                 return Response({'status':'bad request'},status=status.HTTP_200_OK)
#
#             print(title, cover, content, promote, """category_id, """,author_id)
#
#             ### now we have to extract some data like author name and category name not their id and then save them in DB
#             user1 = User.objects.get(id=author_id)
#
#             author=userProfile.objects.get(user=user1)
#
#             #category=Category.objects.get(id=category_id).title
#             category=Category.objects.get(title='xyz')
#
#             ### going to save article on DB
#             article=Article()
#             print("savvvvvvvve1")
#             article.title=title
#             print("savvvvvvvve2")
#             #article.cover=cover
#             print("savvvvvvvve3")
#             article.content=content
#             print("savvvvvvvve4")
#             article.category=category
#             article.author=author
#             print("savvvvvvvve5")
#             article.promote=promote
#             print("savvvvvvvve6")
#             print(article.author)
#             print(article)
#             article.save()
#             print("savvvvvvvve7")
#
#
#
#             return Response({'status':'save done'} ,status=status.HTTP_200_OK)
#
#
#         except:
#             return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SubmitCategoryAPIView(APIView):
    def post(self,request,format=None):
        try:
            serialized_data=serializers.SubmitCategorySerializer(data=request.data)

            if serialized_data.is_valid():
                cat=Category()
                cat.title=serialized_data.data.get('title')
                cat.cover=serialized_data.data.get('cover')
                cat.save()
            else:
                return Response({'status': 'bad request'}, status=status.HTTP_200_OK)

            return Response({'status':'save done'} ,status=status.HTTP_200_OK)

        except:
            return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SubmitArticleAPIView(APIView):
    def post(self,request):
        try:
            serialized_data=serializers.SubmitArticleSerializer(data=request.data)
            print("lllllllllllllllll")
            print(request.POST)
            # tmp=str(serialized_data)
            # data=re.split(',',tmp)
            # for x in data:
            #     print(x,type(x))
            print("title:",request.POST['title'])
            print("contente:", request.POST['content'])
            # print("cover:", serialized_data.data.get('cover'))
            print("promote:", request.POST['promote'])
            print("category:", request.POST['category_id'])
            print("author:", request.POST['author_id'])
            #print((serialized_data.is_valid()))
            #print((serialized_data.errors))
            if serialized_data.is_valid():

                userProfile_object=userProfile.objects.get(id=int(request.POST['author_id']))
                author=userProfile_object
                category_object=Category.objects.get(title='xyz')
                category=category_object
                print("//////////////////////////")
                #print('in if validation : ',author,category)

                article_obj=Article()
                article_obj.title=request.POST['title']
                #article_obj.cover=serialized_data.data.get('cover')
                article_obj.content=request.POST['content']
                article_obj.category=category
                article_obj.author=author
                article_obj.promote=request.POST['promote']

                article_obj.save()
            else:
                return Response({'status': 'bad request'}, status=status.HTTP_200_OK)
            return Response({'status': 'save done'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal server error '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
