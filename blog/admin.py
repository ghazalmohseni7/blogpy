from django.contrib import admin
from .models import Article , userProfile, Category
# Register your models here.
admin.site.register(userProfile)
admin.site.register(Article)
admin.site.register(Category)