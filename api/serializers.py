from rest_framework import serializers
from blog.models import *


class SingleArticleSerializers(serializers.ModelSerializer):
    # title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_legth=250)
    # cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_legth=250)
    # content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_legth=350)
    # created_at = serializers.DateTimeField(required=True, allow_null=False)
    class Meta:
        model = Article
        fields = ('title', 'cover', 'content', 'created_at',)


class SubmitArticleSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True, allow_null=False, allow_blank=False , max_length=250)
    # cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    # content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=350)
    # category_id=serializers.IntegerField(required=False,allow_null=False)
    # author_id=serializers.IntegerField(required=False,allow_null=False)
    # promote=serializers.BooleanField(required=True,allow_null=False)
    #
    class Meta:
        model = Article
        fields = ('title', 'cover', 'content', 'category_id', 'author_id', 'promote',)


class SubmitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'cover')


class UpdateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = ('id', 'title', 'content', 'promote')
        # title , content and promote are the fields that i want to change them


class DeleteArticleSerializer(serializers.Serializer):
    # class Meta:
    #     model = Article
    #     fields = ('id')
    id = serializers.IntegerField(required=True, allow_null=False)
