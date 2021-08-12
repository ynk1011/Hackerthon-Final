from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import elections.views

from django.conf.urls import url

#여긴 사용 안합니다~~
#혹시 몰라서 삭제는 안함

urlpatterns = [
   # path('admin/', admin.site.urls), #주소, 실행할 내용
    #path('', elections.views.index, name="index"),
   # path('areas/<str:area>/', elections.views.areas),
   # path('polls/<int:poll_id>/', elections.views.polls),
   # path('areas/<str:area>/results/', elections.views.results),

    #path("index/<int:area>", elections.views.index, name="index"),


]