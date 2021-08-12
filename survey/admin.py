from django.contrib import admin
from survey.models import Survey, Answer

# Register your models here.

# 관리자 사이트에서 Survey클래스 출력 모양 정의하는 코드


class SurveyAdmin(admin.ModelAdmin):
    # 출력할 필드 목록
    list_display = ("question", "ans1", "ans2", "ans3", "ans4", "status")


# 클래스 등록
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)
