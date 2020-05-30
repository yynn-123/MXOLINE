import xadmin
from apps.courses.models import Course
class CourseAdmin(object):
    list_display = ['id','name','desc','learn_times','category']
    list_filter = ['id', 'name', 'desc', 'learn_times', 'category']
    search_fields=['name','desc']




xadmin.site.register(Course,CourseAdmin)