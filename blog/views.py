from elections.models import Candidate
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog,  HashTag, Comment, Post
from .forms import BlogForm, CommentForm, ResponseForm
# from blog.models import Question
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, request
from django.views.generic import View
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from survey.models import Survey, Answer
import random
from django.db.models import Count, Avg, Min, Max, Sum
from django.contrib import messages
# Create your views here.


def home(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects
    blog = Blog.objects.order_by('-id')
    popular_blog = Blog.objects.order_by('-likes')[:4]
    # query set
    # home.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴
    return render(request, 'home.html', {'blogs': blog, 'postlist': postlist, 'popular_blog': popular_blog})

# 게시판섹션(구 board)의 게시글(posting)을 부르는 posting 함수


def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    #post_detail = get_object_or_404(Post, pk=post_id)
    post_detail = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post': post_detail})

# 디테일 페이지


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(post=blog_id)
    blog_hashtag = blog_detail.hashtag.all()

    survey = Survey.objects.filter(
        status='y').order_by("survey_idx")[blog_id - 1]

    if request.method == "POST":
        comment = Comment()
        # comment.author_name = request.POST['author']
        comment.post = blog_detail
        comment.comment_text = request.POST['body']
        comment.date = timezone.now()
        comment.save()
    return render(request, 'detail.html', {'blog': blog_detail, 'comments': comments, 'hashtags': blog_hashtag, 'survey': survey})


def new(request):  # 글 작성 페이지로 이동
    form = BlogForm()
    return render(request, 'new.html', {'form': form})


def popup(request):
    return render(request, 'popup.html')


def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(",")
        for tag in hashtag:
            ht = HashTag.objects.get_or_create(hashtag_name=tag)
            new_blog.hashtag.add(ht[0])
        # return redirect('detail', new_blog.id)
    return redirect('new_survey')


def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    if blog_detail.author_name == request.user.nickname:
        return render(request, 'edit.html', {'blog': blog_detail})
    else:
        messages.add_message(request, messages.ERROR, '본인 게시글이 아닙니다.')
        return detail(request, blog_id)


def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    blog_update.title = request.POST['title']
    blog_update.body = request.POST['body']
    blog_update.save()
    return redirect('home')


# 게시글 삭제
def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    if blog_delete.author_name == request.user.nickname:
        blog_delete.delete()
        return redirect('home')
    else:
        messages.add_message(request, messages.ERROR, '본인 게시글이 아닙니다.')
        return detail(request, blog_id)


# 댓글...
def add_comment_to_post(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail', blog_id)

    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


# 마이페이지
def mypage(request):
    blogs = Blog.objects.all()
    myblog = blogs.filter(author_name=request.user.nickname)
    return render(request, 'mypage.html', {'blogs': myblog})


# 좋아요 버튼 누르기
def like(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    blog_detail.likes += 1
    blog_detail.save()
    return detail(request, blog_id)


# survey

def main(request):
    return render(request, 'main.html')


def result(request):
    return render(request, 'result.html')


def index(request):
    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    if sort == Blog.objects.order_by('-update_date'):
        return render(request, 'blog/home.html', {'blogs': Blogs})

    else:
        user = request.user
        card = Blogs.objects.filter(name_id=user).order_by(
            '-update_date')  # 복수를 가져올수 있음
        return render(request, 'blog/home.html', {'blogs': Blogs})
