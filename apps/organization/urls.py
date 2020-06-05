
from django.conf.urls import url
from django.urls import include
from apps.organization.views import OrgView
urlpatterns = [

    url(r'^list/', OrgView.as_view(),name='list'),

 ]
