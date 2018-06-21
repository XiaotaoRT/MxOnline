# _*_ encoding: utf-8 _*_
__author__ = 'Admin'
__date__ = '2018/6/4 17:02'


from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentView, AddComentsView, VideoPlayView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    #课程详情页
    url(r'^detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^info/(?P<course_id>.*)/$', CourseInfoView.as_view(), name="course_info"),
    url(r'^comment/(?P<course_id>.*)/$', CommentView.as_view(), name="course_comment"),
    #添加课程评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

    url(r'^video/(?P<video_id>.*)/$', VideoPlayView.as_view(), name="video_play"),
]