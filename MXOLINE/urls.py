"""MXOLINE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# from apps.users import views
from django.views.generic import TemplateView

from apps.organization.views import OrgView
from apps.users.views import LoginView,LoginOutView
from django.conf.urls import url, include
from django.views.static import serve
from MXOLINE.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    #     path('',views.index)
    # 显示首页
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # 显示登陆
    path('login/', LoginView.as_view(), name='login'),
    path('loginout/', LoginOutView.as_view(), name='logout'),
    # 配置授课机构列表展示
    # path('orglist/', OrgView.as_view(), name='org_list'),
    # 配置授课机构相关操作
    url(r'^org/', include(('apps.organization.urls','organization'),namespace='org')),
    # 配置公开课列表展示
    url(r'^course/', include(('apps.courses.urls','courses'),namespace='course')),
    # 配置上传文件的URL
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    #配置用户操作相关
    url(r'^op/',include(('apps.operations.urls','operations'),namespace='op'))
]
