from django.contrib import admin

# Register your models here.
from .models import ArticlePost
from .models import ArticleColumn

admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)