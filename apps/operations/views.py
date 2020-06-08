from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from apps.operations.forms import UserFavForm
from apps.operations.models import UserFavorite
from apps.courses.models import Course
from apps.organization.models import CourseOrg
from apps.organization.models import Teacher
class AddFavView(View):
    """
    用户收藏实现
    """
    # 先判断用户是否登陆
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                'status':'fail',
                'msg':'用户未登录'
            })

        userFavForm = UserFavForm(request.POST)
        if userFavForm.is_valid():
            fav_id = userFavForm.cleaned_data['fav_id']
            fav_type = userFavForm.cleaned_data['fav_type']
            # 判断用户是否已经收藏
            existed_recorder = UserFavorite.objects.filter(user = request.user,fav_id = fav_id,fav_type=fav_type)
            if existed_recorder:
                # 收藏这条信息删除
                existed_recorder.delete()
                if fav_type == 1:
                    course = Course.objects.get(id = fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id = fav_id)
                    course_org.fav_nums -= 1
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id = fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '未收藏 '
                })
            else:
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.user = request.user
                user_fav.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '已收藏 '
                })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '参数错误 '
            })


