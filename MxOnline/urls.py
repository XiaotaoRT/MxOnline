# _*_ encoding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
import xadmin
from django.views.static import serve
from users.views import LogOurView, IndexView, LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, qsView
from MxOnline.settings import MEDIA_ROOT
from MxOnline.settings import STATIC_ROOT
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogOurView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name="forgetpwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^question/$', qsView.as_view(), name="question"),
    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),
    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace="course")),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 生产模式下自动代理静态路径
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 课程相关url配置
    url(r'^teacher/', include('courses.urls', namespace="course")),

    url(r'^users/', include('users.urls', namespace="users")),
    # 富文本相关url
    url(r'^ueditor/', include('DjangoUeditor.urls'))
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'

handler500 = 'users.views.page_error'
