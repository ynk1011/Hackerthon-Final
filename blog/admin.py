from django.contrib import admin
from .models import Blog, Comment, HashTag, Post  # *쓰면 한번에 가능

# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(HashTag)
admin.site.register(Post)
