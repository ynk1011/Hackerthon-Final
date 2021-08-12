from django.db import models

# Create your models here.

# 설문 문항 클래스


class Survey(models.Model):
    # 설문 인덱스
    survey_idx = models.AutoField(primary_key=True)
    # 질문, NOT NULL설정
    question = models.TextField(null=False)
    # 선택지
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    # 설문진행여부 (y=진행중 / n=종료)
    status = models.CharField(max_length=1, default='y')
    


# 설문 응답 클래스
class Answer(models.Model):
    # 응답아이디(자동증가필드!)
    answer_idx = models.AutoField(primary_key=True)
    # 설문아이디(어떤 투표값인지)
    survey_idx = models.IntegerField()
    # 응답번호(어떤 보기에 넣었는가?)
    num = models.IntegerField()
