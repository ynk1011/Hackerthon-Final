from django.db import models
from django.db.models.base import Model
from django.db import models

# Create your models here.

#후보 
class Candidate(models.Model):
    name = models.CharField(max_length=10,default="")
    introduction = models.TextField(null=True, default="")
    party_number = models.IntegerField(default=1)
    area = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)

    #사진추가? 

    def __str__(self):
        return self.name


#투표 (시작 기간, 영역, id)
class Poll(models.Model):
    #startdate = models.DateTimeField()
    #enddate = models.DateTimeField()
    area = models.CharField(max_length = 15)
    id = models.AutoField(primary_key=True)

#선택
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE,)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE,)
    votes = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True)