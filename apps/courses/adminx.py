import xadmin
from .models import Courses, Lesson, Video, CourseResource, BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0


class CoursesAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time', 'course_org']
    # 排序
    ordering = ['-click_nums']
    # 只读
    readonly_fields = ['click_nums']
    # 隐藏与只读冲突
    exclude = ['fav_nums']
    # 增加附属结构
    inlines = [LessonInline]
    # 列表修改内容
    list_editable = ['degree', 'desc']
    # 刷新时间
    #refresh_times = [3]
    style_fields = {"detail": "ueditor"}
    import_excel = True

    def queryset(self):
        qs = super(CoursesAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Courses.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CoursesAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Courses, CoursesAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
