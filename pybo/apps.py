from django.apps import AppConfig

#settings.py의 INSTALLED APPS에 등록하기 위한 정보

#이 클래스 안에 모델에 대한 프로퍼티도 명시되어있다.
class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'
