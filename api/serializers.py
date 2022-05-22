from rest_framework import serializers
from blog.models import *

class SingleArticleSerializers(serializers.ModelSerializer):
    # title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_legth=250)
    # cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_legth=250)
    # content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_legth=350)
    # created_at = serializers.DateTimeField(required=True, allow_null=False)
    class Meta:
        model=Article
        fields=('title','cover','content','created_at',)
