from django.db import models
from django.contrib.auth.models import User
#앱이 데이터베이스를 이용 및 테이블 생성을 위한 정보

#models.py를 수정한다는 것은 데이터베이스 테이블 구성을 수정한다는 것이다.
#이것을 수정한 후에는 꼭 makemigrations명령을 통해 실제 테이블에 반영하기 위한 파일을 먼저 생성해주고
#migrate명령을 통해 그 파일을 실제 테이블에 적용시켜줘야 변화가 실제 테이블에 반영된다.

#모델에 메서드가 추가될 경우에는 makemigrations와 migrate를 수행할 필요가 없다.
#makemigrations, migrate 명령이 필요한 경우는 모델의 속성이 변경되었을때 뿐이다.

# Create your models here.
'''
제목처럼 글자수의 길이가 제한된 텍스트는 CharField를 사용한다. 
내용(content)처럼 글자수를 제한할 수 없는 텍스트는 위처럼 TextField를 사용한다. 
작성일시처럼 날짜와 시간에 관계된 속성은 DateTimeField를 사용한다.
'''
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject



'''
Answer 모델은 질문에 대한 답변에 해당되므로 Question 모델을 속성으로 가져가야 한다. 
기존 모델을 속성으로 연결하려면 ForeignKey를 사용해야 한다. 
ForeignKey는 다른 모델과 연결하기 위해 사용한다. 
on_delete=models.CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미이다.
'''
'''
질문 하나에는 무수히 많은 답변이 등록될 수 있다. 
CASCADE 옵션은 질문을 삭제하면 그에 달린 답변들도 모두 함께 삭제한다.
'''
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')