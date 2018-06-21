# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
from organization.models import CourseOrg, Teacher
# Create your models here.


class Courses(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = UEditorField(u'课程详情', width=600, height=300, imagePath="course/ueditor/", filePath="course/ueditor/", blank=True, default='')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2, verbose_name=u"难度")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    teacher = models.ForeignKey(Teacher, null=True, blank=True, verbose_name=u"讲师")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击量")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u"课程类别")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你能学到什么")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        return self.lesson_set.all().count()
    get_zj_nums.short_description = u"章节数"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程章节
        return self.lesson_set.all()

    def go_to(self):
        # xadmin html显示
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>百度</a>")
    go_to.short_description = u"跳转"


class BannerCourse(Courses):
    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name
        # 防止生成新表
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Courses, verbose_name=u"课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_video(self):
        #获取章节视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节名", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, verbose_name=u"访问地址", default="")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Courses, verbose_name=u"课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="courses/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
