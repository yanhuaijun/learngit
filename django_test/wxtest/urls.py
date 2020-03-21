from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from django.urls import path
from django.conf.urls import url,include
from .views import *
from .robot import *
from .views_weixin import *
# from .views import check
from werobot.contrib.django import make_view

urlpatterns = [
   path('wx/',make_view(robot)),
    path('yanz/',check),
    path('wxindex/', wxindex),
    path('gzhuweixin/', gzhuweixin),
    path('userinfor/', userinfor),
    path('hahaindex/', hahaindex),
    path('fenxindex/', index),
path('ssion/', ssion1),
]
    #path('f/', f),
   # path(r'^life/(?P<nid>\d+)/',life),
    # path('ajax_demo1/', ajax_demo1),
    # path('ajax_add/', ajax_add),
    #path('xx/', xx),

# urlpatterns += staticfiles_urlpatterns()

# url(r'^detail/(\d+)/' ,views.detail)  path('life/1/',a)  (?P<nid>\d+)