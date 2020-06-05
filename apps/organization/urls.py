
from django.conf.urls import url
from django.urls import include
from apps.organization.views import OrgView, Add_Ask

urlpatterns = [

    url(r'^list/$', OrgView.as_view(),name='list'),
    url(r'^add_ask/$', Add_Ask.as_view(),name='add_ask'),

 ]
