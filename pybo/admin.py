#장고의 관리자 기능을 사용해서
#데이터베이스를 관리하기 위한 정보들

#관리자 기능으로 데이터베이스에 직접 접근해서
#CRUD할 수 있다는 것은 엄청난 것이다.

from django.contrib import admin
from .models import Question

# Register your models here.

#admin이라는 도구상자(장고가 고맙게도 미리 준비해준)
#에서 ModelAdmin이라는 도구를 상속받으면
#검색기능을 사용할 수 있다.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#Question테이블과 Question테이블 내의 검색기능을 등록
admin.site.register(Question, QuestionAdmin)