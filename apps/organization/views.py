from django.shortcuts import render

# Create your views here.
from django.views import View


class OrgView(View):
    def get(self,request,*args,**kwargs):
        """
        展示授课机构列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return render(request,'org-list.html')