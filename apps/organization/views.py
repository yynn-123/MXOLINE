from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.organization.models import CourseOrg, Teacher, City
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organization.forms import AddAskForm


class OrgView(View):
    def get(self, request, *args, **kwargs):
        """
        展示授课机构列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_orgs = CourseOrg.objects.all()

        all_cities = City.objects.all()
        hot_orgs = all_orgs.order_by('click_nums')[:3]
        # '?'这种方式传参采用都是采用get方法，首先过去点击类目
        category = request.GET.get('ct', '')

        if category:
            all_orgs = all_orgs.filter(category=category)

        # 对所在城市进行筛选
        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))
        org_nums = all_orgs.count()
        # 对课程机构进行排序, - 代表倒叙排序
        sort = request.GET.get('sort', '')
        # 根据学生人数排序
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            # 根据课程数目进行排序
            all_orgs = all_orgs.order_by('-course_nums')
        org_nums = all_orgs.count()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=5, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html',
                      {
                          'all_orgs': orgs,
                          'org_nums': org_nums,
                          'all_cities': all_cities,
                          'category': category,
                          'city_id': city_id,
                          'sort': sort,
                          'hot_orgs': hot_orgs,
                      }
                      )


class Add_Ask(View):
    """
    处理用户咨询模块
    """

    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                'status': 'success',
                'msg': '提交成功'
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '添加出错'
            })
