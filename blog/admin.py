from django.contrib import admin
from .models import Article, userProfile, Category


# Register your models here.


class userProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']
    search_fields = ['user']


admin.site.register(userProfile, userProfileAdmin)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'category', 'author']
    list_display = ['title', 'author', 'content', 'category']


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Category, CategoryAdmin)
