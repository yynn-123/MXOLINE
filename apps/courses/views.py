from django.core.paginator import PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

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
        # 热门课程推荐
        hot_courses = all_courses.order_by('-click_nums')[:3]
        # 课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=3, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses':hot_courses

        })
