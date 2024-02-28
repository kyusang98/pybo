#페이지 요청이 발생하면 가장 먼저 실행되는 파일
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#django.contrib에서 admin(관리자페이지)기능을
#미리 만들어 놓음 그래서 우리는 그것을 가져다 씀
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

#pybo기능을 우리가 자체 제작하고
#그 기능을 가져다 씀
#from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls), #admin페이지 요청이 발생하면 admin.site.urls 기능으로 연결하세요!
    #path('pybo/',views.index), #pybo페이지 요청이 발생하면 views.index 기능으로 연결하세요!
    path('pybo/', include('pybo.urls')), #pybo페이지 요청이 발생하면 pybo디렉터리의 urls.py를 참조하겠다!
    path('common/',include('common.urls')),
    path('', base_views.index, name='index'), # '/'에 해당되는 path
]
