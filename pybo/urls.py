from django.urls import path
#config의 urls의 깔끔한 작성을 돕는 멀티탭같은 역할


from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    #base_views.py
    path('',base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name = 'detail'),

    #question_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create,name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',question_views.question_modify,name='question_modify'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    #answer_views.py
    path('question/delete/<int:question_id>/',question_views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote,
         name='answer_vote'),
]