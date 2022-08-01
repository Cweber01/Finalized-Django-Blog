from django.contrib import admin
from .models import Post, Comment
# importing 'Post' model made in models.py file within blog
from .models import Post


admin.site.register(Post)
admin.site.register(Comment)
