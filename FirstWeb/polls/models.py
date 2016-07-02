from django.db import models

# Create your models here.
class Question(models.Model):
    # 질문 필드(최대 문자열 길이 200)
    question_text = models.CharField(max_length=200)
    # 질문 등록시간 필드
    pub_date = models.DateTimeField('date published')

    # 테이블명 설
    def __str__(self): # 파이썬2.7에선 __unicode__
        return self.question_text

class Choice(models.Model):
    # 답변,질문 연결 필드
    question = models.ForeignKey(Question)
    # 답변 문구 필드(최대 문자열 길이 200)
    choice_text = models.CharField(max_length=200)
    # 답변수 계측 필드(기본값 0)
    votes = models.IntegerField(default=0)

    # 테이블정명 설정
    def __str__(self): # 파이썬2.7에선 __unicode__
        return self.choice_text