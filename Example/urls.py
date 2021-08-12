"""Example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from survey import views

import blog.views as blog
import account.views as account
# import elections.views
import survey.views as survey


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.home, name="home"),
    path("blog/<int:blog_id>", blog.detail, name="detail"),
    path('new/', blog.new, name="new"),
    path('create/', blog.create, name="create"),
    path('edit/<int:blog_id>', blog.edit, name="edit"),
    path('update/<int:blog_id>', blog.update, name="update"),
    path('delete/<int:blog_id>', blog.delete, name="delete"),
    path('<int:blog_id>/comment', blog.add_comment_to_post,
         name="add_comment_to_post"),
    path('mypage/', blog.mypage, name="mypage"),
    path('account/login', account.login_view, name="login"),
    path('account/logout', account.logout_view, name="logout"),
    path('account/register', account.register_view, name="register"),

    path('new_survey/', survey.new_survey, name="new_survey"),
    path('create_survey/', survey.create_survey, name="create_survey"),

    path('like/<int:blog_id>', blog.like, name="like"),

    # # 투표(구버전)
    # path('index/', elections.views.index, name="index"),
    # path('index/areas/<int:area>/', elections.views.areas, name="areas"),
    # path('polls/<int:poll_id>/', elections.views.polls, name="polls"),
    # path('areas/<str:area>/results/', elections.views.results,  name="results"),
    # path('index/areas/클릭/results/', elections.views.jump, name="jump"),
    # path('electionhome/', elections.views.electionhome, name="electionhome"),
    # path('newelection/', elections.views.newelection, name="newelection"),
    # path('electionhome2/', elections.views.electionhome2, name="electionhome2"),
    # path('newelection2/', elections.views.newelection2, name="newelection2"),
    # path('pollhome/', elections.views.pollhome, name="pollhome"),
    # path('newpoll/', elections.views.newpoll, name="newpoll"),
    # path('choicehome/', elections.views.choicehome, name="choicehome"),
    # path('newchoice/', elections.views.newchoice, name="newchoice"),
    # path('choicehome2/', elections.views.choicehome2, name="choicehome2"),
    # path('newchoice2/', elections.views.newchoice2, name="newchoice2"),




    # 설문조사 관련 URL
    url(r'^$', views.main),  # localhost
    url(r'^save_survey$', views.save_survey),
    url(r'^show_result', views.show_result),

    path('main/<int:blog_id>', survey.main, name="main"),
    path('show_result/', survey.show_result, name="show_result"),
    path('save_survey/', survey.save_survey, name="save_survey"),

    # 게시판 연결
    path("posting/<int:pk>", blog.posting, name="posting"),

    path('popup/', blog.popup, name="popup"),

    # 투표 랜덤 추천
    #path("blog/<int:blog_id>", blog.random_post, name="random_post"),
    #url(r'^random_post$', blog.random_post),
    #url(r'^random_post/(?P<num>[0-9]+)', blog.random_post, name='random_post'),

]


# 디버깅관련 URL

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
