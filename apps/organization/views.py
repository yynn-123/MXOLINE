from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.organization.models import CourseOrg, Teacher, City


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
        org_nums = CourseOrg.objects.all().count()

        all_cities = City.objects.all()

        return render(request, 'org-list.html',
                      {
                          'all_orgs': all_orgs,
                          'org_nums': org_nums,
                          'all_cities': all_cities,
                      }
                      )
