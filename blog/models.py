from account.models import CustomUser
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.conf import settings



# Create your models here.


class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag_name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hashtag = models.ManyToManyField(HashTag)
    author_name = models.CharField(max_length=10,default='')
    likes = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.title

    def summary_body(self):
        return self.body[:20]

    def summary_title(self):
        return self.title[:10]


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE, null=True)
    author_name = models.CharField(max_length=20, default='')
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def apporve(self):
        self.save()

    def __str__(self):
        return self.comment_text


# 게시판

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    id = models.AutoField(primary_key=True)
        
    def __str__(self):
        return self.postname[:20]
