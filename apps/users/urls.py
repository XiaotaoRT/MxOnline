# _*_ encoding: utf-8 _*_
__author__ = 'Admin'
__date__ = '2018/6/7 23:29'

from django.conf.urls import url
from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCoudeView, UpdateEmailCoudeView
from .views import MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    url(r'^sendemail_code/$', SendEmailCoudeView.as_view(), name="sendemail_code"),
    url(r'^updatemail_code/$', UpdateEmailCoudeView.as_view(), name="update_email"),
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    # 我收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),
]