from django.core.paginator import PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.operations.models import UserFavorite
from apps.courses.models import Course


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """
        获取课程列表信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_courses = Course.objects.all().order_by('-add_time')
        # 最热门和参与人数排序
        sort = request.GET.get('sort', '')
        if sort == 'hot':
            # 最热门
            all_courses = all_courses.order_by('-click_nums')
        elif sort == 'students':
            # 参与人数
            all_courses = all_courses.order_by('-students')
        else:
            all_courses = all_courses.order_by('add_time')
        # 热门课程推荐
        hot_courses = all_courses.order_by('add_time')[:3]
        # 课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=20, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses

        })


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 根据id查询课程
        course = Course.objects.get(id=int(course_id))
        # 点击到课程详情就记录一次点击数
        course.click_nums += 1
        course.save()
        has_fav_course = False
        has_fav_org = False
        # 获取收藏状态
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构fav_type=1证明是课程收藏，如果有，证明用户收藏了这个课程
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=2):
                has_fav_org = True
        return render(request, 'course-detail.html', {
            'course': course,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org,
        })
