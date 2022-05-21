from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
import os


# Create your models here.

def validateFileExtension(value):
    fileExtension = os.path.splitext(value.name)[1]
    validateExtensions = ['.jpg', '.png']
    if fileExtension.lower() not in validateExtensions:
        raise ValidationError('unsupported extension')


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='pics/userAvatar/', null=True, blank=True, validators=[validateFileExtension])
    description = models.TextField(max_length=250, null=False, blank=False)
    def __str__(self):
        return self.user.username



class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='pics/categoryCover/', null=False, blank=False, validators=[validateFileExtension])
    def __str__(self):
        return self.title



class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='pics/articleCover/', null=True, blank=True, validators=[validateFileExtension])
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    promote=models.BooleanField(default=False)
    def __str__(self):
        return self.title



