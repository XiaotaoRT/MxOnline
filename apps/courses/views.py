# _*_ encoding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite, CourseComments, UserCourse
from .models import Courses, CourseResource, Video
from utils.mixin_utils import LoginRequiredMixin
# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_course = Courses.objects.all().order_by("-add_time")
        hot_courses = Courses.objects.all().order_by("-click_nums")[:3]
        #课程搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_course = all_course.filter(Q(name__icontains=search_keywords)|
                                           Q(desc__icontains=search_keywords)|
                                           Q(detail__icontains=search_keywords))

        # 课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-students")
            elif sort == "hot":
                all_course = all_course.order_by("-click_nums")

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 3, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_course': courses,
            'sort': sort,
            'hot_courses': hot_courses
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Courses.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org_id, fav_type=2):
                has_fav_org = True
        tag = course.tag
        if tag:
            relat_courses = Courses.objects.filter(tag=tag).all()[:1]
        else:
            relat_courses =[]
        return render(request, "course-detail.html", {
            'course': course,
            'relat_courses': relat_courses,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org
        })


class CourseInfoView(LoginRequiredMixin, View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Courses.objects.get(id=int(course_id))

        # 查询用户是否已经关联了该课程
        user_cour = UserCourse.objects.filter(user=request.user, course=course)
        if not user_cour:
            user_cour = UserCourse(user=request.user, course=course)
            user_cour.save()
            course.students += 1
            course.save()

        # 取出所有学过该课程的用户
        user_courses = UserCourse.objects.filter(course=course)
        # 取用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 获取其他用户学过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学过所有课程的点击排名
        relate_courses = Courses.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,
        })


class CommentView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Courses.objects.get(id=int(course_id))
        # 取出所有学过该课程的用户
        user_courses = UserCourse.objects.filter(course=course)
        # 取用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 获取其他用户学过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学过所有课程的点击排名
        relate_courses = Courses.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all().order_by("-add_time")
        return render(request, "course-comment.html", {
            'course': course,
            'all_resources': all_resources,
            'all_comments': all_comments,
            'relate_courses': relate_courses
        })

class AddComentsView(View):
    """
    用户添加课程评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if int(course_id) > 0 and comments:
            course_comments = CourseComments()
            course = Courses.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加失败"}', content_type='application/json')


class VideoPlayView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course
        # 查询用户是否已经关联了该课程
        user_cour = UserCourse.objects.filter(user=request.user, course=course)
        if not user_cour:
            user_cour = UserCourse(user=request.user, course=course)
            user_cour.save()
            course.students += 1
            course.save()

        # 取出所有学过该课程的用户
        user_courses = UserCourse.objects.filter(course=course)
        # 取用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 获取其他用户学过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学过所有课程的点击排名
        relate_courses = Courses.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-play.html", {
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,
            'video': video
        })