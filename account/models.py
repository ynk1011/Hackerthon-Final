from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    GENDERS = (
        ('M', '남성'),
        ('F', '여성')
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS, default = '')

    JOBS = (
        ('S', '학생'),
        ('O', '직장인'),
        ('F', '프리랜서'),
        ('E', '기타')
    )
    job = models.CharField(verbose_name='직업', max_length=1, choices=JOBS, default = '')

    age=models.IntegerField(default=1)

    nickname = models.CharField(max_length=20, default='')

    
